import unittest
from providers.bttv import parseEmote

EMOTES = [
    {
        "id": "566ca38765dbbdab32ec0560",
        "code": "SourPls",
        "imageType": "gif",
        "animated": True,
        "userId": "5561169bd6b9d206222a8c19",
        "modifier": False,
    },
    {
        "id": "5e76d399d6581c3724c0f0b8",
        "code": "cvMask",
        "imageType": "png",
        "animated": False,
        "userId": "54ee2465b822020506c52a52",
        "modifier": False,
    },
]

class TestParsing(unittest.TestCase):
    def test_code(self):
        for i, value in enumerate([
                'SourPls',
                'cvMask',
            ]):
            emote = parseEmote(EMOTES[i])
            self.assertEqual(emote.toDict()['code'], value)

    def test_provider(self):
        for e in EMOTES:
            emote = parseEmote(e)
            self.assertEqual(emote.toDict()['provider'], 2)

    def test_zero_width(self):
        for i, value in enumerate([
                False,
                True,
            ]):
            emote = parseEmote(EMOTES[i])
            self.assertEqual(emote.toDict()['zero_width'], value)

    def test_animated(self):
        for i, value in enumerate([
                True,
                False,
            ]):
            emote = parseEmote(EMOTES[i])
            self.assertEqual(emote.toDict()['animated'], value)

    def test_urls(self):
        for i, value in enumerate([
                [
                    {
                        "size": "1x",
                        "url": "https://cdn.betterttv.net/emote/566ca38765dbbdab32ec0560/1x"
                    },
                    {
                        "size": "2x",
                        "url": "https://cdn.betterttv.net/emote/566ca38765dbbdab32ec0560/2x"
                    },
                    {
                        "size": "3x",
                        "url": "https://cdn.betterttv.net/emote/566ca38765dbbdab32ec0560/3x"
                    }
                ],
                [
                    {
                        "size": "1x",
                        "url": "https://cdn.betterttv.net/emote/5e76d399d6581c3724c0f0b8/1x"
                    },
                    {
                        "size": "2x",
                        "url": "https://cdn.betterttv.net/emote/5e76d399d6581c3724c0f0b8/2x"
                    },
                    {
                        "size": "3x",
                        "url": "https://cdn.betterttv.net/emote/5e76d399d6581c3724c0f0b8/3x"
                    }
                ],
            ]):
            emote = parseEmote(EMOTES[i])
            self.assertEqual(emote.toDict()['urls'], value)

if __name__ == '__main__':
    unittest.main()
