from abc import ABC, abstractmethod
from typing import Any, Union, Callable

from waio.rules.abc import ABCRule
from waio.types import Message


class ABCHandler(ABC):

    @abstractmethod
    def __init__(self, handler: Callable, *rules: ABCRule):
        self.handler = handler
        self.rules = rules

    @abstractmethod
    async def filter(self, event: "Message") -> Union[dict, bool]:
        pass

    @abstractmethod
    async def handle(self, event: "Message", **context) -> Any:
        pass
