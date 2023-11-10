import unittest
from providers.ffz import parseEmote
import json

with open('test/ffz_global.json', 'r') as file:
    data = json.load(file)

def getEmote(set, code):
    return [d for d in data['sets'][str(set)]['emoticons'] if d['name'] == code][0]

EMOTES = [
    getEmote(3, 'ZliL'),
]

class TestParsing(unittest.TestCase):
    def test_code(self):
        for i, value in enumerate([
                'ZliL',
            ]):
            emote = parseEmote(EMOTES[i])
            self.assertEqual(emote.toDict()['code'], value)

    def test_provider(self):
        for e in EMOTES:
            emote = parseEmote(e)
            self.assertEqual(emote.toDict()['provider'], 3)

    def test_zero_width(self):
        for e in EMOTES:
            emote = parseEmote(e)
            self.assertEqual(emote.toDict()['zero_width'], False)

    def test_animated(self):
        for e in EMOTES:
            emote = parseEmote(e)
            self.assertEqual(emote.toDict()['animated'], False)

    def test_urls(self):
        for i, value in enumerate([
                [
                    {
                        "size": "1x",
                        "url": "https://cdn.frankerfacez.com/emote/28138/1"
                    },
                    {
                        "size": "2x",
                        "url": "https://cdn.frankerfacez.com/emote/28138/2"
                    },
                    {
                        "size": "4x",
                        "url": "https://cdn.frankerfacez.com/emote/28138/4"
                    }
                ],
            ]):
            emote = parseEmote(EMOTES[i])
            self.assertEqual(emote.toDict()['urls'], value)

if __name__ == '__main__':
    unittest.main()
