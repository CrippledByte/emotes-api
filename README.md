# emotes-api
Fetches Twitch emotes from various providers (Twitch, 7TV, BTTV, FFZ).

[![Clang analysis](https://status.crippled.dev/api/badge/5/status)](https://emotes.crippled.dev)

# Endpoints
- `/v1/channel/<username>/<provider>`
- `/v1/global/<provider>`

Available providers: `twitch`, `7tv`, `bttv`, `ffz`, `all`.

## Output
```json
[
  {
    "animated": false,
    "code": "FeelsDankMan",
    "provider": 1,
    "urls": [
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
    "zero_width": false
  },
  ...
]
```

### Providers
| id | Provider |
| --- | --- |
| 0 | Twitch |
| 1 | 7TV |
| 2 | BTTV |
| 3 | FFZ |

# Setup
1. Register an app on [dev.twitch.tv](https://dev.twitch.tv/console/apps/create) and enter the client ID and secret in [.env](.env.example).
2. Install requirements.
```python
pip3 install -r requirements.txt
```
3. Run the server.
```python
gunicorn --preload --bing 0.0.0.0:8000 app:app
```

# Development
- Unit tests
```python
python3 -m unittest
```
