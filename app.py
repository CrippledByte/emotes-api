from flask import Flask, jsonify
from flask_compress import Compress
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging
from cachetools import LRUCache, cached
from dotenv import load_dotenv
import os
from models.channel import Channel

# Providers
# 0: Twitch
# 1: 7TV
# 2: BTTV
# 3: FFZ

channels = {}

print("Starting server..")

# Flask
app = Flask(__name__)
CORS(app)
Compress(app)
limiter = Limiter(app, key_func=get_remote_address, headers_enabled=True)

load_dotenv()
CACHE_CHANNEL_LIMIT = int(os.getenv('CACHE_CHANNEL_LIMIT', 500))
MAX_CACHE_TTL = int(os.getenv('MAX_CACHE_TTL', 300))

cache = LRUCache(maxsize=CACHE_CHANNEL_LIMIT)

def custom_error(status_code, message):
    response = jsonify({
        'status_code': status_code,
        'message': message
    })
    response.status_code = status_code
    app.logger.warning('Returning error: %s %s', status_code, message)
    return response

@app.errorhandler(404)
def not_found(error):
    return custom_error(404, 'Page not found.')

@app.errorhandler(429)
def rate_limit_exceeded(error):
    return custom_error(429, 'Rate limit exceeded. Please slow down (60 requests per minute).')

if (MAX_CACHE_TTL > 0):
    @app.after_request
    def add_header(response):
        response.headers['Cache-Control'] = f'max-age={MAX_CACHE_TTL}'
        return response

@app.route('/')
def index():
    return jsonify({
        'global': '/v1/global/<provider>',
        'channel': '/v1/channel/<username>/<provider>',
        'providers': ['twitch', '7tv', 'bttv', 'ffz', 'all'],
    })

@cached(cache)
def get_channel(login):
    return Channel(login)

def get_emotes(login, provider):
    channel = get_channel(login)

    if provider == 'twitch':
        return jsonify(channel.getTwitchEmotes())
    elif provider == '7tv':
        return jsonify(channel.getSevenTVEmotes())
    elif provider == 'bttv':
        return jsonify(channel.getBTTVEmotes())
    elif provider == 'ffz':
        return jsonify(channel.getFFZEmotes())
    elif provider == 'all':
        return jsonify(channel.getEmotes())

    return custom_error(404, 'Provider not found.')

@app.route('/v1/global/<provider>')
@limiter.limit("60/minute")
def global_emotes(provider):
    return get_emotes('_global', provider)

@app.route('/v1/channel/<login>/<provider>')
@limiter.limit("60/minute")
def channel_emotes(login, provider):
    return get_emotes(login, provider)

if __name__ == '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.run(host='0.0.0.0', threaded=True, port=5000, debug=True)
