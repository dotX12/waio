from typing import Dict

import ujson


class MessageText:
    def __init__(self, text: str):
        self.type = "text"
        self.text = text

    def dict(self) -> Dict[str, str]:
        return {"type": self.type, "text": self.text}

    def json(self) -> str:
        return ujson.dumps(self.dict(), indent=2)
