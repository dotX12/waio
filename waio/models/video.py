from typing import Optional

import ujson


class VideoModel:
    def __init__(
            self,
            url: str,
            caption: Optional[str] = None

    ):
        self.type = 'video'
        self.url = url
        self.caption = caption

    def dict(self):
        return {
            "type": self.type,
            "url": self.url,
            "caption": self.caption,
        }

    def json(self):
        return ujson.dumps(self.dict(), indent=2)
