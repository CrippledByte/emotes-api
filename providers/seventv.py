from dotenv import load_dotenv
import time
import os
import requests
from models.emotes import Emote

base_url = 'https://7tv.io/v3'

load_dotenv()
CACHE_TIMEOUT = int(os.getenv('CACHE_TIMEOUT_7TV', 300))

EmoteFlagsZeroWidth = 1 << 8 # https://github.com/SevenTV/Common/blob/4139fcc3eb8d79003573b26b552ef112ec85b8df/structures/v3/type.emote.go#L52

def parseEmote(e):
    emote = Emote(
        code=e['name'],
        provider=1,
        zero_width=(e['data']['flags'] & EmoteFlagsZeroWidth) != 0,
        animated=e['data']['animated']
    )

    host = e['data']['host']
    template = 'https:' + host['url']
    for file in host['files']:
        if file['format'] != 'WEBP':
            continue
        size = file['name'].replace('.webp', '')
        url = f"{template}/{file['name']}"
        emote.addUrl(size, url)

    return emote

def updateEmotes(self):
    if (time.time() - self.seventv_emotes_updated) < CACHE_TIMEOUT:
        print(f'[{self.login}] Using cached 7tv emotes.')
        return

    print(f'[{self.login}] Updating 7tv emotes..')
    self.seventv_emotes.clear()

    emotes = []
    if self.login == '_global':
        # Get global emote set
        url = f'{base_url}/emote-sets/global'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            emotes.extend(data['emotes'])
    else:
        # Get user connection which contains active emote set
        url = f'{base_url}/users/twitch/{self.user_id}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            emotes.extend(data['emote_set']['emotes'])

    for e in emotes:
        emote = parseEmote(e)
        self.seventv_emotes.append(emote)

    self.seventv_emotes_updated = time.time()
    print(f'[{self.login}] Updated 7tv emotes: {len(self.seventv_emotes)} emotes.')

def getEmotes(self):
    with self.seventv_lock:
        updateEmotes(self)
        return [e.toDict() for e in self.seventv_emotes]
