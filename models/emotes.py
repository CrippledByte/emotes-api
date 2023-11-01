class EmoteUrl:
    def __init__(self, size, url):
        self.size = size
        self.url = url

    def toDict(self):
       return dict(size=self.size, url=self.url)

class Emote:
    def __init__(self, code, provider, zero_width, animated):
        self.code = code
        self.provider = provider
        self.zero_width = zero_width
        self.animated = animated
        self.urls = []

    def toDict(self):
        return dict(
            code=self.code,
            provider=self.provider,
            zero_width=self.zero_width,
            animated = self.animated,
            urls=[u.toDict() for u in self.urls]
        )

    def addUrl(self, size, url):
        self.urls.append(EmoteUrl(size, url))
