from typing import Union, Optional, Dict, Any

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

    async def finish(self, clear_data: Optional[bool] = False) -> None:
        await self.storage.finish_state(key=self.user)
        if clear_data:
            await self.storage.finish_data(key=self.user)

    async def set_data(self, **kwargs: Union[str, int]) -> bool:
        return await self.storage.set_data(self.user, **kwargs)

    async def get_data(self, *data_keys) -> Dict[str, Union[str, int]]:
        data_values = await self.storage.get_data(key=self.user)
        if data_keys:
            return {key: value for key, value in data_values.items() if key in data_keys}
        return data_values
