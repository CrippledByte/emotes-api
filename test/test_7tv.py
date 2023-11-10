import unittest
from providers.seventv import parseEmote

EMOTES = [
    {
      "id": "63071bb9464de28875c52531",
      "name": "FeelsDankMan",
      "flags": 0,
      "timestamp": 1661580705379,
      "actor_id": "603b7c7496832ffa78522da5",
      "data": {
        "id": "63071bb9464de28875c52531",
        "name": "FeelsDankMan",
        "flags": 0,
        "lifecycle": 3,
        "state": [
          "LISTED"
        ],
        "listed": True,
        "animated": False,
        "owner": {
          "id": "603cb1c696832ffa78cc3bc2",
          "username": "clyvere",
          "display_name": "clyverE",
          "avatar_url": "//static-cdn.jtvnw.net/jtv_user_pictures/3ff40972-0188-4cfc-adbf-8db119d7cf2a-profile_image-70x70.png",
          "style": {},
          "roles": [
            "62b48deb791a15a25c2a0354"
          ]
        },
        "host": {
          "url": "//cdn.7tv.app/emote/63071bb9464de28875c52531",
          "files": [
            {
              "name": "1x.avif",
              "static_name": "1x_static.avif",
              "width": 28,
              "height": 32,
              "frame_count": 1,
              "size": 1193,
              "format": "AVIF"
            },
            {
              "name": "1x.webp",
              "static_name": "1x_static.webp",
              "width": 28,
              "height": 32,
              "frame_count": 1,
              "size": 1148,
              "format": "WEBP"
            },
            {
              "name": "2x.avif",
              "static_name": "2x_static.avif",
              "width": 56,
              "height": 64,
              "frame_count": 1,
              "size": 1975,
              "format": "AVIF"
            },
            {
              "name": "2x.webp",
              "static_name": "2x_static.webp",
              "width": 56,
              "height": 64,
              "frame_count": 1,
              "size": 2672,
              "format": "WEBP"
            },
            {
              "name": "3x.avif",
              "static_name": "3x_static.avif",
              "width": 84,
              "height": 96,
              "frame_count": 1,
              "size": 2956,
              "format": "AVIF"
            },
            {
              "name": "3x.webp",
              "static_name": "3x_static.webp",
              "width": 84,
              "height": 96,
              "frame_count": 1,
              "size": 4858,
              "format": "WEBP"
            },
            {
              "name": "4x.avif",
              "static_name": "4x_static.avif",
              "width": 112,
              "height": 128,
              "frame_count": 1,
              "size": 3869,
              "format": "AVIF"
            },
            {
              "name": "4x.webp",
              "static_name": "4x_static.webp",
              "width": 112,
              "height": 128,
              "frame_count": 1,
              "size": 6392,
              "format": "WEBP"
            }
          ]
        }
      }
    },
    {
      "id": "62e5c88ba1a665fe6efd5aa2",
      "name": "TeaTime",
      "flags": 0,
      "timestamp": 1661364136976,
      "actor_id": "603b7c7496832ffa78522da5",
      "data": {
        "id": "62e5c88ba1a665fe6efd5aa2",
        "name": "TeaTime",
        "flags": 0,
        "lifecycle": 3,
        "state": [
          "LISTED"
        ],
        "listed": True,
        "animated": True,
        "owner": {
          "id": "60f5e290e57bec021618c4a4",
          "username": "ansonx10",
          "display_name": "AnsonX10",
          "avatar_url": "//cdn.7tv.app/user/60f5e290e57bec021618c4a4/av_63617cc39018da6429bc0298/3x_static.webp",
          "style": {
            "color": 401323775
          },
          "roles": [
            "60b3f1ea886e63449c5263b1",
            "62b48deb791a15a25c2a0354"
          ]
        },
        "host": {
          "url": "//cdn.7tv.app/emote/62e5c88ba1a665fe6efd5aa2",
          "files": [
            {
              "name": "1x.avif",
              "static_name": "1x_static.avif",
              "width": 32,
              "height": 32,
              "frame_count": 61,
              "size": 13064,
              "format": "AVIF"
            },
            {
              "name": "1x.webp",
              "static_name": "1x_static.webp",
              "width": 32,
              "height": 32,
              "frame_count": 61,
              "size": 10332,
              "format": "WEBP"
            },
            {
              "name": "2x.avif",
              "static_name": "2x_static.avif",
              "width": 64,
              "height": 64,
              "frame_count": 61,
              "size": 12108,
              "format": "AVIF"
            },
            {
              "name": "2x.webp",
              "static_name": "2x_static.webp",
              "width": 64,
              "height": 64,
              "frame_count": 61,
              "size": 11072,
              "format": "WEBP"
            },
            {
              "name": "3x.webp",
              "static_name": "3x_static.webp",
              "width": 96,
              "height": 96,
              "frame_count": 61,
              "size": 14020,
              "format": "WEBP"
            },
            {
              "name": "3x.avif",
              "static_name": "3x_static.avif",
              "width": 96,
              "height": 96,
              "frame_count": 61,
              "size": 19636,
              "format": "AVIF"
            },
            {
              "name": "4x.webp",
              "static_name": "4x_static.webp",
              "width": 128,
              "height": 128,
              "frame_count": 61,
              "size": 12536,
              "format": "WEBP"
            },
            {
              "name": "4x.avif",
              "static_name": "4x_static.avif",
              "width": 128,
              "height": 128,
              "frame_count": 61,
              "size": 14119,
              "format": "AVIF"
            }
          ]
        }
      }
    },
    {
      "id": "612fc78b9a14cebbb339b113",
      "name": "SteerR",
      "flags": 1,
      "timestamp": 1657657167712,
      "actor_id": None,
      "data": {
        "id": "612fc78b9a14cebbb339b113",
        "name": "SteerR",
        "flags": 256,
        "lifecycle": 3,
        "state": [
          "LISTED",
          "NO_PERSONAL"
        ],
        "listed": True,
        "animated": True,
        "owner": {
          "id": "60ae81ff0bf2ee96aea05247",
          "username": "snortexx",
          "display_name": "snortexx",
          "avatar_url": "//cdn.7tv.app/pp/60ae81ff0bf2ee96aea05247/183b9b6ab7624a53966fb782ec0963e0",
          "style": {},
          "roles": [
            "62b48deb791a15a25c2a0354"
          ]
        },
        "host": {
          "url": "//cdn.7tv.app/emote/612fc78b9a14cebbb339b113",
          "files": [
            {
              "name": "1x.avif",
              "static_name": "1x_static.avif",
              "width": 32,
              "height": 32,
              "frame_count": 20,
              "size": 7367,
              "format": "AVIF"
            },
            {
              "name": "1x.webp",
              "static_name": "1x_static.webp",
              "width": 32,
              "height": 32,
              "frame_count": 20,
              "size": 8014,
              "format": "WEBP"
            },
            {
              "name": "2x.webp",
              "static_name": "2x_static.webp",
              "width": 64,
              "height": 64,
              "frame_count": 20,
              "size": 14098,
              "format": "WEBP"
            },
            {
              "name": "2x.avif",
              "static_name": "2x_static.avif",
              "width": 64,
              "height": 64,
              "frame_count": 20,
              "size": 12198,
              "format": "AVIF"
            },
            {
              "name": "3x.avif",
              "static_name": "3x_static.avif",
              "width": 96,
              "height": 96,
              "frame_count": 20,
              "size": 20659,
              "format": "AVIF"
            },
            {
              "name": "3x.webp",
              "static_name": "3x_static.webp",
              "width": 96,
              "height": 96,
              "frame_count": 20,
              "size": 23168,
              "format": "WEBP"
            },
            {
              "name": "4x.avif",
              "static_name": "4x_static.avif",
              "width": 128,
              "height": 128,
              "frame_count": 20,
              "size": 18107,
              "format": "AVIF"
            },
            {
              "name": "4x.webp",
              "static_name": "4x_static.webp",
              "width": 128,
              "height": 128,
              "frame_count": 20,
              "size": 21800,
              "format": "WEBP"
            }
          ]
        }
      }
    },
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
