from typing import Optional, TypeVar
import aioredis

T = TypeVar("T", bound="RedisConnector")


class RedisConnector:
    def __init__(self, redis_url: str, db_number: int = 1, encoding: Optional[str] = "utf-8"):
        self._redis: Optional[aioredis.Redis] = None
        self.redis_url = redis_url
        self.db = db_number
        self.encoding = encoding

    @property
    def redis(self) -> aioredis.Redis:
        if not self.check_connection:
            self.create_session()
        return self._redis

    @property
    def check_connection(self) -> bool:
        conn_attr = hasattr(self._redis, 'connection')
        if conn_attr:
            if self._redis.connection:
                return True
        return False

    def create_session(self) -> None:
        self._redis = aioredis.from_url(url=self.redis_url, encoding=self.encoding, db=self.db, decode_responses=True)

    async def close_session(self) -> None:
        await self._redis.close()
