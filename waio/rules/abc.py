from abc import ABC, abstractmethod
from typing import Union


class ABCRule(ABC):

    @abstractmethod
    async def check(self, message) -> Union[dict, bool]:
        pass
