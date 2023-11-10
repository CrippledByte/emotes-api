import unittest
from providers.ffz import parseEmote

EMOTES = [
    {
        "id": 28138,
        "name": "ZliL",
        "height": 23,
        "width": 32,
        "public": False,
        "hidden": True,
        "modifier": False,
        "modifier_flags": 0,
        "offset": None,
        "margins": None,
        "css": None,
        "owner": {
            "_id": 1,
            "name": "sirstendec",
            "display_name": "SirStendec"
        },
        "artist": None,
        "urls": {
            "1": "https://cdn.frankerfacez.com/emote/28138/1",
            "2": "https://cdn.frankerfacez.com/emote/28138/2",
            "4": "https://cdn.frankerfacez.com/emote/28138/4"
        },
        "status": 1,
        "usage_count": 1,
        "created_at": "2015-06-03T00:37:44.041Z",
        "last_updated": "2015-06-04T20:22:11.432Z"
    },
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
