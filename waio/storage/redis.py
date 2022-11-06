import ujson
from typing import Optional, Any, Dict, Union

from waio.storage.connector import RedisConnector


class RedisStorage(RedisConnector):
    def __init__(self, redis_url: str, prefix_fsm: str = "fsm", db: int = 1):
        super().__init__(redis_url=redis_url, db_number=db)
        self.prefix_fsm = prefix_fsm

    def _generate_key_state(self, key) -> str:
        return f"{self.prefix_fsm}:{key}:state"

    def _generate_key_data(self, key) -> str:
        return f"{self.prefix_fsm}:{key}:data"

    async def _set(self, key: str, value: Any) -> bool:
        _value = ujson.dumps(value)
        set_response = await self.redis.set(name=key, value=_value)
        return bool(set_response)

    async def _key_availability(self, key) -> bool:
        key_exist = await self.redis.exists(key)
        if key_exist:
            return True
        return False

    async def _base_get(self, key) -> Dict[Union[str, int], Any]:
        value = await self.redis.get(name=key)
        value_dict = ujson.loads(value)
        return value_dict

    async def set(self, key, value) -> bool:
        if await self._key_availability(key=key):
            key_value = await self._base_get(key=key)
            new_values = {**key_value, **value}
            return await self._set(key, new_values)
        else:
            return await self._set(key, value)

    async def set_state(self, key, value) -> bool:
        fsm_key_state = self._generate_key_state(key=key)
        state_dict = {"state": str(value)}
        return await self.set(key=fsm_key_state, value=state_dict)

    async def get_state(self, key) -> Optional[str]:
        key_state = self._generate_key_state(key=key)
        query = await self.redis.get(name=key_state)
        if query:
            query_state = ujson.loads(query)
            if query_state.get("state"):
                return query_state["state"]
        return None

    async def finish_state(self, key) -> None:
        key_state = self._generate_key_state(key=key)
        await self.redis.delete(key_state)

    async def set_data(self, key, **kwargs) -> bool:
        fsm_key_data = self._generate_key_data(key=key)
        return await self.set(key=fsm_key_data, value=kwargs)

    async def get_data(self, key):
        key = self._generate_key_data(key=key)
        return await self._base_get(key)

    async def finish_data(self, key) -> None:
        key_data = self._generate_key_data(key=key)
        await self.redis.delete(key_data)
