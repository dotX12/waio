from typing import Optional

import ujson


class ImageModel:
    def __init__(
        self,
        original_url: str,
        preview_url: Optional[str] = None,
        caption: Optional[str] = None
    ):
        self.type = 'image'
        self.original_url = original_url
        self.preview_url = preview_url or original_url
        self.caption = caption

    def dict(self):
        return {
            "type": self.type,
            "originalUrl": self.original_url,
            "previewUrl": self.preview_url,
            "caption": self.caption,
        }

    def json(self):
        return ujson.dumps(self.dict(), indent=2)
