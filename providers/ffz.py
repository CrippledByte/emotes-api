from dotenv import load_dotenv
import time
import os
import requests
from models.emotes import Emote

base_url = 'https://api.frankerfacez.com/v1'

load_dotenv()
CACHE_TIMEOUT = int(os.getenv('CACHE_TIMEOUT_FFZ', 300))

def parseEmote(e):
    emote = Emote(
        code=e['name'],
        provider=3,
        zero_width=False,
        animated='animated' in e.keys()
    )

    for u in (e.get('animated') or e['urls']).items():
        size = f'{u[0]}x'
        url = u[1]
        emote.addUrl(size, url)

    return emote

def updateEmotes(self):
    if (time.time() - self.ffz_emotes_updated) < CACHE_TIMEOUT:
        print(f'[{self.login}] Using cached ffz emotes.')
        return

    print(f'[{self.login}] Updating ffz emotes..')
    self.ffz_emotes.clear()

    emotes = []
    if self.login == '_global':
        url = f'{base_url}/set/global'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            set_ids = data['default_sets']

            for set_id in set_ids:
                emotes.extend(data['sets'][str(set_id)]['emoticons'])
    else:
        url = f'{base_url}/room/id/{self.user_id}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            set_id = data['room']['set']
            emotes.extend(data['sets'][str(set_id)]['emoticons'])

    for e in emotes:
        emote = parseEmote(e)
        self.ffz_emotes.append(emote)

    self.ffz_emotes_updated = time.time()
    print(f'[{self.login}] Updated ffz emotes: {len(self.ffz_emotes)} emotes.')

def getEmotes(self):
    with self.ffz_lock:
        updateEmotes(self)
        return [e.toDict() for e in self.ffz_emotes]
