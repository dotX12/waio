from typing import Dict

import ujson


class StickerModel:
    def __init__(
        self,
        url: str,
    ):
        self.type = "sticker"
        self.url = url

    def dict(self) -> Dict[str, str]:
        return {
            "type": self.type,
            "url": self.url,
        }

    def json(self) -> str:
        return ujson.dumps(self.dict(), indent=2)
