from typing import Optional

import ujson


class FileModel:
    def __init__(
            self,
            url: str,
            filename: str,
            caption: Optional[str] = None
    ):
        self.type = 'file'
        self.url = url
        self.filename = filename
        self.caption = caption

    def dict(self):
        return {
            "type": self.type,
            "url": self.url,
            "filename": self.filename,
            "caption": self.caption,
        }

    def json(self):
        return ujson.dumps(self.dict(), indent=2)
