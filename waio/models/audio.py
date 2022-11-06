from typing import Dict

import ujson


class AudioModel:
    def __init__(
        self,
        url: str,
    ):
        self.type = "audio"
        self.url = url

    def dict(self) -> Dict[str, str]:
        return {
            "type": self.type,
            "url": self.url,
        }

    def json(self) -> str:
        return ujson.dumps(self.dict(), indent=2)
