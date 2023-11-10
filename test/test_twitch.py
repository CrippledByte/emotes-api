import unittest
import twitchAPI
from providers.twitch import parseEmote

TEMPLATE = 'https://static-cdn.jtvnw.net/emoticons/v2/{{id}}/{{format}}/{{theme_mode}}/{{scale}}'
EMOTES = [
    twitchAPI.object.api.Emote(
        id='25',
        name='Kappa',
        images={
            'url_1x': 'https://static-cdn.jtvnw.net/emoticons/v2/25/static/light/1.0',
            'url_2x': 'https://static-cdn.jtvnw.net/emoticons/v2/25/static/light/2.0',
            'url_4x': 'https://static-cdn.jtvnw.net/emoticons/v2/25/static/light/3.0'
        },
        format=[
            'static'
        ],
        scale=[
            '1.0',
            '2.0',
            '3.0'
        ],
        theme_mode=[
            'light',
            'dark'
        ]
    ),
    twitchAPI.object.api.Emote(
        id='emotesv2_dcd06b30a5c24f6eb871e8f5edbd44f7',
        name='DinoDance',
        images={
            "url_1x": "https://static-cdn.jtvnw.net/emoticons/v2/emotesv2_dcd06b30a5c24f6eb871e8f5edbd44f7/static/light/1.0",
            "url_2x": "https://static-cdn.jtvnw.net/emoticons/v2/emotesv2_dcd06b30a5c24f6eb871e8f5edbd44f7/static/light/2.0",
            "url_4x": "https://static-cdn.jtvnw.net/emoticons/v2/emotesv2_dcd06b30a5c24f6eb871e8f5edbd44f7/static/light/3.0"
        },
        format=[
            "static",
            "animated"
        ],
        scale=[
            "1.0",
            "2.0",
            "3.0"
        ],
        theme_mode=[
            "light",
            "dark"
        ]
    )
]

class TestParsing(unittest.TestCase):
    def test_code(self):
        for i, value in enumerate([
                'Kappa',
                'DinoDance',
            ]):
            emote = parseEmote(EMOTES[i], TEMPLATE)
            self.assertEqual(emote.toDict()['code'], value)

    def test_provider(self):
        for e in EMOTES:
            emote = parseEmote(e, TEMPLATE)
            self.assertEqual(emote.toDict()['provider'], 0)

    def test_zero_width(self):
        for e in EMOTES:
            emote = parseEmote(e, TEMPLATE)
            self.assertEqual(emote.toDict()['zero_width'], False)

    def test_animated(self):
        for i, value in enumerate([
                False,
                True,
            ]):
            emote = parseEmote(EMOTES[i], TEMPLATE)
            self.assertEqual(emote.toDict()['animated'], value)

    def test_urls(self):
        for i, value in enumerate([
                [
                    {
                        "size": "1x",
                        "url": "https://static-cdn.jtvnw.net/emoticons/v2/25/default/light/1.0"
                    },
                    {
                        "size": "2x",
                        "url": "https://static-cdn.jtvnw.net/emoticons/v2/25/default/light/2.0"
                    },
                    {
                        "size": "3x",
                        "url": "https://static-cdn.jtvnw.net/emoticons/v2/25/default/light/3.0"
                    }
                ],
                [
                    {
                        "size": "1x",
                        "url": "https://static-cdn.jtvnw.net/emoticons/v2/emotesv2_dcd06b30a5c24f6eb871e8f5edbd44f7/default/light/1.0"
                    },
                    {
                        "size": "2x",
                        "url": "https://static-cdn.jtvnw.net/emoticons/v2/emotesv2_dcd06b30a5c24f6eb871e8f5edbd44f7/default/light/2.0"
                    },
                    {
                        "size": "3x",
                        "url": "https://static-cdn.jtvnw.net/emoticons/v2/emotesv2_dcd06b30a5c24f6eb871e8f5edbd44f7/default/light/3.0"
                    }
                ],
            ]):
            emote = parseEmote(EMOTES[i], TEMPLATE)
            self.assertEqual(emote.toDict()['urls'], value)

if __name__ == '__main__':
    unittest.main()
