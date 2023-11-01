from dotenv import load_dotenv
from twitchAPI.twitch import Twitch
import asyncio
import time
import os
from providers.twitch import parseTwitchEmote
import threading

load_dotenv()
CACHE_TIMEOUT = int(os.getenv('CACHE_TIMEOUT', 300))
TWITCH_CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
TWITCH_SECRET = os.getenv('TWITCH_SECRET')

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
        self.lock = threading.Lock()

        if login != '_global':
            asyncio.run(self.getUserId())

    async def updateTwitchEmotes(self):
        if (time.time() - self.twitch_emotes_updated) < CACHE_TIMEOUT:
            print(f'[{self.login}] Using cached twitch emotes.')
            return

        print(f'[{self.login}] Updating twitch emotes..')
        self.twitch_emotes.clear()
        twitch = await Twitch(TWITCH_CLIENT_ID, TWITCH_SECRET)

        if self.login == '_global':
            emotes = await twitch.get_global_emotes()
        else:
            emotes = await twitch.get_channel_emotes(self.user_id)
        for e in emotes:
            emote = parseTwitchEmote(e, emotes.template)
            self.twitch_emotes.append(emote)

        self.twitch_emotes_updated = time.time()
        print(f'[{self.login}] Updated twitch emotes: {len(self.twitch_emotes)} emotes.')

    def getTwitchEmotes(self):
        with self.lock:
            asyncio.run(self.updateTwitchEmotes())
            return [e.toDict() for e in self.twitch_emotes]
