from abc import ABC
from typing import Any
from typing import Dict
from typing import Optional

from waio.handlers import ABCHandler
from waio.types import Event


class BaseMiddleware(ABC):

    event: Event
    handler: Optional[ABCHandler]
    response: Optional[Dict[str, Any]]

    def fill(
        self,
        event: Event,
        response: Optional[Dict[str, Any]] = None,
        handler: Optional[ABCHandler] = None,
    ):
        self.event = event
        self.handler = handler
        self.response = response

    async def pre(self):
        pass

    async def post(self):
        pass

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__} "
            f"event: {self.event}, "
            f"handler: {self.handler}, "
            f"return: {self.response}>"
        )
