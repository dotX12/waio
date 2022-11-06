from abc import ABC, abstractmethod
from typing import Union
from waio.types import Event


class ABCRule(ABC):

    @abstractmethod
    async def check(self, event: Event) -> Union[dict, bool]:
        raise NotImplemented
