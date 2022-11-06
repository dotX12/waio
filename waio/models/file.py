from typing import Dict
from typing import Optional
from typing import Union

import ujson


class FileModel:
    def __init__(self, url: str, filename: str, caption: Optional[str] = None):
        self.type = "file"
        self.url = url
        self.filename = filename
        self.caption = caption

    def dict(self) -> Dict[str, Union[str, None]]:
        return {
            "type": self.type,
            "url": self.url,
            "filename": self.filename,
            "caption": self.caption,
        }

    def json(self) -> str:
        return ujson.dumps(self.dict(), indent=2)
