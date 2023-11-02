from dotenv import load_dotenv
import time
import os
import requests
from models.emotes import Emote

base_url = 'https://api.betterttv.net/3'

load_dotenv()
CACHE_TIMEOUT = int(os.getenv('CACHE_TIMEOUT', 300))

# https://github.com/Chatterino/chatterino2/blob/1043f9f8037ed53fbaf1812f289a4e3db152e140/src/providers/twitch/TwitchMessageBuilder.cpp#L51
# https://github.com/flex3r/DankChat/blob/9aa32300df8c71ef84758d0d8a9196616fc8a526/app/src/main/kotlin/com/flxrs/dankchat/data/repo/EmoteRepository.kt#L612
ZERO_WIDTH = [
		"SoSnowy", "IceCold", "SantaHat", "TopHat",
		"ReinDeer", "CandyCane", "cvMask", "cvHazmat"
]

def parseBTTVEmote(e):
    emote = Emote(
        code=e['code'],
        provider=2,
        zero_width=e['code'] in ZERO_WIDTH,
        animated=e['animated']
    )

    for size in ['1x', '2x', '3x']:
        url = f"https://cdn.betterttv.net/emote/{e['id']}/{size}"
        emote.addUrl(size, url)

    return emote

def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z

def updateBTTVEmotes(self):
    if (time.time() - self.bttv_emotes_updated) < CACHE_TIMEOUT:
        print(f'[{self.login}] Using cached bttv emotes.')
        return

    print(f'[{self.login}] Updating bttv emotes..')
    self.bttv_emotes.clear()

    emotes = []
    if self.login == '_global':
        url = f'{base_url}/cached/emotes/global'
        response = requests.get(url)
        if response.status_code == 200:
            emotes = response.json()
    else:
        url = f'{base_url}/cached/users/twitch/{self.user_id}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            emotes.extend(data['channelEmotes'])
            emotes.extend(data['sharedEmotes'])

    for e in emotes:
        emote = parseBTTVEmote(e)
        self.bttv_emotes.append(emote)

    self.bttv_emotes_updated = time.time()
    print(f'[{self.login}] Updated bttv emotes: {len(self.bttv_emotes)} emotes.')

def getBTTVEmotes(self):
    with self.bttv_lock:
        updateBTTVEmotes(self)
        return [e.toDict() for e in self.bttv_emotes]
