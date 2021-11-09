import ujson
from typing import Union, List, Optional
from waio.keyboard.list import ListMainButton


class KeyboardButton(ListMainButton):
    def __init__(self, title: str):
        super().__init__(title)


class QuickReplyContentBase:
    def __init__(self, text: str, caption: str):
        self.text = text
        self.caption = caption


class QuickReplyContentText(QuickReplyContentBase):
    def __init__(self, header: str, text: str, caption: str):
        self.type = "text"
        self.header = header

        super().__init__(text, caption)

    def json(self):
        return {
            "type": self.type,
            "header": self.header,
            "text": self.text,
            "caption": self.caption
        }


class QuickReplyContentImage(QuickReplyContentBase):
    def __init__(self, url: str, text: str, caption: str):
        self.type = "image"
        self.url = url

        super().__init__(text, caption)

    def json(self):
        return {
            "type": self.type,
            "url": self.url,
            "text": self.text,
            "caption": self.caption
        }


class QuickReplyContentDocument(QuickReplyContentBase):
    def __init__(self, url: str, filename: str, text: str, caption: str):
        self.type = "file"
        self.url = url
        self.filename = filename

        super().__init__(text, caption)

    def json(self):
        return {
            "type": self.type,
            "url": self.url,
            "text": self.text,
            "caption": self.caption,
            "filename": self.filename
        }


class QuickReplyContentVideo(QuickReplyContentBase):
    def __init__(self, url: str, text: str, caption: str):
        self.type = "video"
        self.url = url

        super().__init__(text, caption)

    def json(self):
        return {
            "type": self.type,
            "url": self.url,
            "text": self.text,
            "caption": self.caption,
        }


class QuickReply:
    def __init__(
            self,
            callback_data: str,
            content: Union[
                QuickReplyContentText,
                QuickReplyContentImage,
                QuickReplyContentDocument,
                QuickReplyContentVideo
            ],
            options: Optional[List[KeyboardButton]] = None
    ):
        self.type = "quick_reply"
        self.callback_data = callback_data
        self.content = content

        if options is None:
            self.options = []
        else:
            self.options = options

    def add(self, element: KeyboardButton) -> 'QuickReply':
        self.options.append(element)
        return self

    def dict(self):
        return {
            "type": self.type,
            "msgid": self.callback_data,
            "content": self.content.json(),
            "options": [element.json() for element in self.options]
        }

    def json(self):
        return ujson.dumps(self.dict(), indent=2)
