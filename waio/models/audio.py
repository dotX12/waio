import ujson


class AudioModel:
    def __init__(
            self,
            url: str,
    ):
        self.type = 'audio'
        self.url = url

    def dict(self):
        return {
            "type": self.type,
            "url": self.url,
        }

    def json(self):
        return ujson.dumps(self.dict(), indent=2)
