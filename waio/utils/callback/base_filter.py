from abc import ABC, abstractmethod
from typing import Dict, Any

from waio.types import Message
from waio.utils.callback.base_callback import CallbackDataBase


class CallbackDataFilterBase(ABC):

    def __init__(self, factory: CallbackDataBase, config: Dict[str, str]):
        self.config = config
        self.factory = factory

    @classmethod
    def validate(cls, full_config: Dict[str, Any]):
        raise ValueError("That filter can't be used in filters factory!")

    async def base_check(self, data):
        try:
            data = self.factory.parse(data)
        except ValueError:
            return False
        for key, value in self.config.items():
            if isinstance(value, (list, tuple, set, frozenset)):
                if data.get(key) not in value:
                    return False
            elif data.get(key) != value:
                return False
        return {'callback_data': data}

    @abstractmethod
    async def check(self, message: Message):
        pass
