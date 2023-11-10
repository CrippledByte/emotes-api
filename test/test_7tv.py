import unittest
from providers.seventv import parseEmote
import json

with open('test/7tv_global.json', 'r') as file:
    data = json.load(file)

def getEmote(code):
    return [d for d in data['emotes'] if d['name'] == code][0]

EMOTES = [
    getEmote('FeelsDankMan'),
    getEmote('TeaTime'),
    getEmote('SteerR'),
]

class TestParsing(unittest.TestCase):
    def test_code(self):
        for i, value in enumerate([
                'FeelsDankMan',
                'TeaTime',
                'SteerR',
            ]):
            emote = parseEmote(EMOTES[i])
            self.assertEqual(emote.toDict()['code'], value)

    def test_provider(self):
        for e in EMOTES:
            emote = parseEmote(e)
            self.assertEqual(emote.toDict()['provider'], 1)

    def test_zero_width(self):
        for i, value in enumerate([
                False,
                False,
                True,
            ]):
            emote = parseEmote(EMOTES[i])
            self.assertEqual(emote.toDict()['zero_width'], value)

    def test_animated(self):
        for i, value in enumerate([
                False,
                True,
                True,
            ]):
            emote = parseEmote(EMOTES[i])
            self.assertEqual(emote.toDict()['animated'], value)

    def test_urls(self):
        for i, value in enumerate([
                [
                    {
                        "size": "1x",
                        "url": "https://cdn.7tv.app/emote/63071bb9464de28875c52531/1x.webp"
                    },
                    {
                        "size": "2x",
                        "url": "https://cdn.7tv.app/emote/63071bb9464de28875c52531/2x.webp"
                    },
                    {
                        "size": "3x",
                        "url": "https://cdn.7tv.app/emote/63071bb9464de28875c52531/3x.webp"
                    },
                    {
                        "size": "4x",
                        "url": "https://cdn.7tv.app/emote/63071bb9464de28875c52531/4x.webp"
                    }
                ],
                [
                    {
                        "size": "1x",
                        "url": "https://cdn.7tv.app/emote/62e5c88ba1a665fe6efd5aa2/1x.webp"
                    },
                    {
                        "size": "2x",
                        "url": "https://cdn.7tv.app/emote/62e5c88ba1a665fe6efd5aa2/2x.webp"
                    },
                    {
                        "size": "3x",
                        "url": "https://cdn.7tv.app/emote/62e5c88ba1a665fe6efd5aa2/3x.webp"
                    },
                    {
                        "size": "4x",
                        "url": "https://cdn.7tv.app/emote/62e5c88ba1a665fe6efd5aa2/4x.webp"
                    }
                ],
                [
                    {
                        "size": "1x",
                        "url": "https://cdn.7tv.app/emote/612fc78b9a14cebbb339b113/1x.webp"
                    },
                    {
                        "size": "2x",
                        "url": "https://cdn.7tv.app/emote/612fc78b9a14cebbb339b113/2x.webp"
                    },
                    {
                        "size": "3x",
                        "url": "https://cdn.7tv.app/emote/612fc78b9a14cebbb339b113/3x.webp"
                    },
                    {
                        "size": "4x",
                        "url": "https://cdn.7tv.app/emote/612fc78b9a14cebbb339b113/4x.webp"
                    }
                ],
            ]):
            emote = parseEmote(EMOTES[i])
            self.assertEqual(emote.toDict()['urls'], value)

if __name__ == '__main__':
    unittest.main()
