from dotenv import load_dotenv
from twitchAPI.twitch import Twitch
import asyncio
import os
import threading
import providers.twitch
import providers.bttv

load_dotenv()
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
        self.twitch_lock = threading.Lock()
        self.bttv_emotes = []
        self.bttv_emotes_updated = 0
        self.bttv_lock = threading.Lock()
        self.login = login

        if login != '_global':
            asyncio.run(self.getUserId())

    def getTwitchEmotes(self):
        return providers.twitch.getTwitchEmotes(self)

    def getBTTVEmotes(self):
        return providers.bttv.getBTTVEmotes(self)

    def getEmotes(self):
        twitch_emotes = self.getTwitchEmotes()
        bttv_emotes = self.getBTTVEmotes()
        return twitch_emotes + bttv_emotes
