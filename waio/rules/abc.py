from abc import ABC, abstractmethod
from typing import Union


class ABCRule(ABC):

    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    async def check(self, message) -> Union[dict, bool]:
        pass
