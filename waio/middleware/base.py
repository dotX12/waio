from abc import ABC
from typing import List, Any, Dict, Optional

from waio.handlers import ABCHandler
from waio.types import Message


class BaseMiddleware(ABC):

    event: Message
    handle_responses: Optional[List[Dict[str, Any]]]
    handlers: Optional[List[ABCHandler]]

    def fill(
            self,
            event: Message,
            handle_responses: Optional[List[Dict[str, Any]]] = None,
            handlers: Optional[List[ABCHandler]] = None,
    ):
        self.event = event
        self.handle_responses = handle_responses
        self.handlers = handlers

    async def pre(self):
        pass

    async def post(self):
        pass

    def __repr__(self) -> str:
        return (f"<{self.__class__.__name__} "
                f"event: {self.event}, "
                f"handlers: {self.handlers}, "
                f"returns: {self.handle_responses}>")
