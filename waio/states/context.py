from typing import Union

from waio.states.fsm import BaseState
from waio.storage.redis import RedisStorage


class FSMContext:
    def __init__(self, storage: RedisStorage, user_phone: int):
        self.storage = storage
        self.user = user_phone

    async def set_state(self, value: BaseState) -> bool:
        return await self.storage.set_state(key=self.user, value=value)

    async def get_state(self) -> str:
        return await self.storage.get_state(key=self.user)

    async def finish(self):
        return await self.storage.finish_state(key=self.user)

    async def set_data(self, **kwargs: Union[str, int]):
        return await self.storage.set_data(self.user, **kwargs)

    async def get_data(self):
        key = self.storage.generate_key_data(key=self.user)
        return await self.storage.base_get(key)
