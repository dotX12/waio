from abc import abstractmethod, ABC
from typing import Union, Dict, Any

from waio.types import Message
from waio.utils.callback.callbacks import CallbackItem, CallbackList


class CallbackDataFilterBase(ABC):

    def __init__(self, factory: Union[CallbackItem, CallbackList], config: Dict[str, str]):
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
