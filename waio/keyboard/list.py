from typing import Optional, Union, List
import ujson

from waio.utils.dicts import clear_none_values


class ListMainButton:
    def __init__(self, title: str):
        self.type = 'text'
        self.title = title

    def json(self):
        return {"type": self.type, "title": self.title}


class ListGroupItem:
    def __init__(
            self,
            title: str,
            callback_data: Optional[str] = None,
            description: Optional[str] = None,
    ):
        self.type = 'text'
        self.title = title  # Maximum length: 24 characters
        self.description = description  # Maximum length: 72 characters
        self.callback_data = callback_data

    def json(self):
        return {
            "type": self.type,
            "title": self.title,
            "description": self.description,
            "postbackText": self.callback_data
        }


class ListGroup:
    def __init__(self, title: str, subtitle: str):
        self.title = title
        self.subtitle = subtitle
        self.options: List[ListGroupItem] = []

    def add(self, list_item: ListGroupItem) -> 'ListGroup':
        self.options.append(list_item)
        return self

    def json(self):

        d = {
            "title": self.title,
            "subtitle": self.subtitle,
            "options": [option.json() for option in self.options],
        }
        return clear_none_values(d)


class ListMessage:
    def __init__(
            self,
            title: str,
            body: str,
            button_title: str,
            items: Optional[List[ListGroup]] = None,
            callback_data: Optional[Union[int, str]] = None,
    ):
        self.type = 'list'
        self.title = title
        self.body = body
        self.button_title = button_title
        self.callback_data = callback_data

        if items is None:
            self.items = []
        else:
            self.items = items

    @property
    def main_button(self):
        return ListMainButton(title=self.button_title)

    def json(self):
        d = {
            "type": self.type,
            "title": self.title,
            "body": self.body,
            "msgid": self.callback_data,
            "globalButtons": [self.main_button.json()],
            "items": [item.json() for item in self.items]
        }
        return ujson.dumps(d, indent=2)
