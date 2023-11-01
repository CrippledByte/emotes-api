from dotenv import load_dotenv
from twitchAPI.twitch import Twitch
import asyncio
import os
import threading
import providers.twitch

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
        self.login = login
        self.lock = threading.Lock()

        if login != '_global':
            asyncio.run(self.getUserId())

    def getTwitchEmotes(self):
        return providers.twitch.getTwitchEmotes(self)
