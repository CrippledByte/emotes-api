from flask import Flask, jsonify
from flask_compress import Compress
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging
from twitchAPI.twitch import Twitch
import os
from dotenv import load_dotenv
import asyncio
import time

# Providers
# 0: Twitch
# 1: 7TV
# 2: BTTV
# 3: FFZ

CACHE_TIMEOUT = 300 # Emote cache duration in seconds

load_dotenv()
TWITCH_CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
TWITCH_SECRET = os.getenv('TWITCH_SECRET')

global_emotes_twitch = []
global_emotes_twitch_updated = 0

channels = {}

class EmoteUrl:
    def __init__(self, size, url):
        self.size = size
        self.url = url

    def toDict(self):
       return dict(size=self.size, url=self.url)

class Emote:
    def __init__(self, code, provider, zero_width, animated):
        self.code = code
        self.provider = provider
        self.zero_width = zero_width
        self.animated = animated
        self.urls = []

    def toDict(self):
        return dict(
            code=self.code,
            provider=self.provider,
            zero_width=self.zero_width,
            animated = self.animated,
            urls=[u.toDict() for u in self.urls]
        )

    def addUrl(self, size, url):
        self.urls.append(EmoteUrl(size, url))

def parseTwitchEmote(e, template):
    emote = Emote(
        code=e.name,
        provider=0,
        zero_width=False,
        animated='animated' in e.format
    )

    for scale in e.scale:
        values = {
            'id': e.id,
            'format': 'default',
            'theme_mode': e.theme_mode[0],
            'scale': scale,
        }
        url = template.replace('{{', '{').replace('}}', '}').format(**values)
        size = f"{int(float(scale))}x"
        emote.addUrl(size, url)

    return emote

# Twitch API
async def update_twitch_global_emotes():
    global global_emotes_twitch_updated
    if (time.time() - global_emotes_twitch_updated) < CACHE_TIMEOUT:
        print('Using cached global twitch emotes.')
        return

    print('Updating global twitch emotes..')
    global_emotes_twitch.clear()

    twitch = await Twitch(TWITCH_CLIENT_ID, TWITCH_SECRET)
    emotes = await twitch.get_global_emotes()
    for e in emotes:
        emote = parseTwitchEmote(e, emotes.template)
        global_emotes_twitch.append(emote)

    global_emotes_twitch_updated = time.time()
    print(f'Updated global twitch emotes: {len(global_emotes_twitch)} emotes.')

class Channel:
    async def getUserId(self):
        twitch = await Twitch(TWITCH_CLIENT_ID, TWITCH_SECRET)
        async for user in twitch.get_users(logins=self.login):
            self.user_id = user.id
            print(f'[{self.login}] Found user: {self.user_id}')

    def __init__(self, login):
        self.twitch_emotes = []
        self.twitch_emotes_updated = 0
        self.login = login
        asyncio.run(self.getUserId())

    async def updateTwitchEmotes(self):
        if (time.time() - self.twitch_emotes_updated) < CACHE_TIMEOUT:
            print(f'[{self.login}] Using cached twitch emotes.')
            return

        print(f'[{self.login}] Updating twitch emotes..')
        self.twitch_emotes.clear()
        twitch = await Twitch(TWITCH_CLIENT_ID, TWITCH_SECRET)
        emotes = await twitch.get_channel_emotes(self.user_id)
        for e in emotes:
            emote = parseTwitchEmote(e, emotes.template)
            self.twitch_emotes.append(emote)

        self.twitch_emotes_updated = time.time()
        print(f'[{self.login}] Updated twitch emotes: {len(self.twitch_emotes)} emotes.')

    def getTwitchEmotes(self):
        asyncio.run(self.updateTwitchEmotes())
        return [e.toDict() for e in self.twitch_emotes]

print("Starting server..")

# Flask
app = Flask(__name__)
CORS(app)
Compress(app)
limiter = Limiter(app, key_func=get_remote_address)

def custom_error(status_code, message):
    response = jsonify({
        'status_code': status_code,
        'message': message
    })
    response.status_code = status_code
    app.logger.warning('Returning error:', status_code, message)
    return response

@app.errorhandler(429)
def rate_limit_exceeded(error):
    return custom_error(429, 'Rate limit exceeded. Please slow down (60 requests per minute).')

@app.route('/global/<provider>')
@limiter.limit("60/minute")
def global_emotes(provider):
    if provider == 'twitch':
        print('Twitch emotes requested.')
        asyncio.run(update_twitch_global_emotes())
        return jsonify([e.toDict() for e in global_emotes_twitch])

    return custom_error(404, 'Provider not found.')

@app.route('/channel/<login>/<provider>')
@limiter.limit("60/minute")
def channel_emotes(login, provider):
    if login not in channels:
        channels[login] = Channel(login)

    if provider == 'twitch':
        return jsonify(channels[login].getTwitchEmotes())

    return custom_error(404, 'Provider not found.')

if __name__ == '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.run(host='0.0.0.0', threaded=True, port=5000, debug=True)
