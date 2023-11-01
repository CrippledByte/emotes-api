from models.emotes import Emote

def parseTwitchEmote(e, template):
    emote = Emote(
        code=e.name,
        provider=0,
        zero_width=False,
        animated='animated' in e.format
    )

    for scale in e.scale:
        values = {
            'id': e.id,
            'format': 'default',
            'theme_mode': e.theme_mode[0],
            'scale': scale,
        }
        url = template.replace('{{', '{').replace('}}', '}').format(**values)
        size = f"{int(float(scale))}x"
        emote.addUrl(size, url)

    return emote
