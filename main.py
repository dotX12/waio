import asyncio
import re

import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

from waio.bot import Bot, Dispatcher
from waio.middleware import BaseMiddleware
from waio.middlewares.type import MiddlewareResponse
from waio.rules.abc import ABCMessageRule
from waio.rules.default import TextRule, TextRuleEquals
from waio.types.content_types import ContentType
from waio.types.message import Message
from waio.states.context import FSMContext
from waio.states.fsm import StatesGroup, BaseState
from waio.storage.redis import RedisStorage
from env import PHONE_NUMBER, SRC_NAME, API_KEY

app = FastAPI()
bot = Bot(
    apikey=API_KEY,
    src_name=SRC_NAME,
    phone_number=PHONE_NUMBER)

storage = RedisStorage(prefix_fsm='fsm', redis_url="redis://localhost:6379")
dp = Dispatcher(bot=bot, storage=storage)


class BanMiddleware(BaseMiddleware):
    def __init__(self):
        self.BAN_PHONES = [79189781010, 79189781009]

    async def pre(self, message: Message):
        if message.message.payload.sender.phone in self.BAN_PHONES:
            return {"example_key_middleware": "example_value_middleware"}
        return True


dp.labeler.register_middleware(BanMiddleware)


class FooState(StatesGroup):
    name = BaseState()
    age = BaseState()
    email = BaseState()
    end = BaseState()


def rate_limit(limit: int, key=None):
    def decorator(func):
        setattr(func, 'throttling_rate_limit', limit)
        if key:
            setattr(func, 'throttling_key', key)
        return func
    return decorator


@dp.message_handler(text_startswitch='121')
@rate_limit(10, 'foos')
async def foo(message: Message, state: FSMContext):
    await message.bot.send_message(79189781008, 'start_swith 121')


@app.post("/api/v1/gupshup/hook")
async def foo(request: Request):
    event = await request.json()
    # print(event)
    await dp.handle_event(event)
    return Response(status_code=200)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8017, debug=True, reload=True)
