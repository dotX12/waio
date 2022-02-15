import ujson


class StickerModel:
    def __init__(
            self,
            url: str,
    ):
        self.type = 'sticker'
        self.url = url

    def dict(self):
        return {
            "type": self.type,
            "url": self.url,
        }

    def json(self):
        return ujson.dumps(self.dict(), indent=2)
