from dotenv import load_dotenv
from twitchAPI.twitch import Twitch
import time
import os
import asyncio
from models.emotes import Emote

load_dotenv()
CACHE_TIMEOUT = int(os.getenv('CACHE_TIMEOUT_TWITCH', 300))
TWITCH_CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
TWITCH_SECRET = os.getenv('TWITCH_SECRET')

def parseEmote(e, template):
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

async def updateEmotes(self):
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
        emote = parseEmote(e, emotes.template)
        self.twitch_emotes.append(emote)

    self.twitch_emotes_updated = time.time()
    print(f'[{self.login}] Updated twitch emotes: {len(self.twitch_emotes)} emotes.')

def getEmotes(self):
    with self.twitch_lock:
        asyncio.run(updateEmotes(self))
        return [e.toDict() for e in self.twitch_emotes]
