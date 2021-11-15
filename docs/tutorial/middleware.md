# Middlewares

## What is this?
Middleware - the so-called outer layers that cover the handling of the handlers. Middleware has two states - pre and post, pre is what happens before the search for the handler starts (when the desired view has just been found), and post is what happens when the handler has already been processed and everything about the processed is known: which handlers worked, what did they return

## Make middlewares
To make a middleware at first you should import the necessary modules
```python
from waio.middleware import BaseMiddleware, MiddlewareResponse, CancelHandler, ContinueHandler
from examples.middleware.database import ExampleDatabase
```

Now start writing your own class
```python
class BanMiddleware(BaseMiddleware):
```

Now let's figure out how to implement the pre and post methods

### async def pre(self):
pre receives only an event (for example, a message) and can return waio.middleware.MiddlewareResponse or dict

In this actor (in this function implemented by you), you can do some checks. If Middleware Response(False) returns from pre, then event processing at all levels will stop urgently, so you can, for example, filter out some spam messages or messages from ignored users. If dict is returned from middleware, it will be unpacked into one handler (await your_handler(event, **dict))

An example of filtering out blocked users:
```python
from waio.middleware import BaseMiddleware, MiddlewareResponse, CancelHandler, ContinueHandler


class BanMiddleware(BaseMiddleware):
    def __init__(self):
        self.BAN_PHONES = [79283334455, 79283334477, 79185554433]

    async def pre(self):
        if self.event.message.payload.sender.phone in self.BAN_PHONES:
            await self.event.answer('Sorry, you are blocked.')
            return MiddlewareResponse(CancelHandler)
        return MiddlewareResponse(ContinueHandler)
```

### async def post(self)

post receives much more information in contrast to pre, but it can no longer affect the processing of the event in any way. It is usually used for statistics and logs. <br>
<br>
Also, using this method you can use the database <br>
Let's create ExampleDatabase class in a file database.py
```python
from typing import Dict, Any


class ExampleDatabase:
    def __init__(self):
        self.session: str = "CLOSED"
        self.data: Dict[str, Any] = {}

    def open_session(self) -> None:
        self.session = 'OPEN'

    def close_session(self) -> None:
        self.session = 'CLOSED'

    @property
    def connection(self) -> bool:
        if self.session == 'CLOSED':
            raise Exception('Database is closed...')
        return True

    def set(self, key, value) -> None:
        if self.connection:
            self.data[key] = value

    def get(self, key) -> Any:
        if self.connection:
            return self.data[key]
```
Next, we will create a middleware using the previously created class
```python
from waio.logs import logger
from waio.middleware import BaseMiddleware, MiddlewareResponse, CancelHandler, ContinueHandler
from examples.middleware.database import ExampleDatabase

class DatabaseMiddleware(BaseMiddleware):
    def __init__(self):
        self.session = ExampleDatabase()

    async def pre(self):
        self.session.open_session()
        self.session.set('key_pre', 'value')

        logger.info(f'[PRE]-DatabaseMiddleware conn: {self.session.session} values: {self.session.data}')
        return {"session": self.session}

    async def post(self):
        self.session.set('key_post', 'value')
        self.session.close_session()

        logger.info(f'[POST]-DatabaseMiddleware conn: {self.session.session} values: {self.session.data}')
```

_pre and post can be used simultaneously in the same middleware_

### Middleware registration

Registration of middleware occurs through the dispatcher <br>
file: misc.py
```python
from waio.bot import Bot, Dispatcher
from waio.logs import loguru_filter

from examples.middleware.example_middlewares import BanMiddleware, DatabaseMiddleware

loguru_filter.set_level('DEBUG')

bot = Bot(
    apikey='API_KEY',
    src_name='SRC_NAME',
    phone_number=0000000000
)

dp = Dispatcher(bot=bot)

dp.labeler.register_middleware(BanMiddleware())
dp.labeler.register_middleware(DatabaseMiddleware())
```

## Using middlewares in handlers
main.py
```python
from aiohttp import web
from waio.types import Message

from examples.middleware.database import ExampleDatabase
from examples.middleware.misc import *

webhook = web.Application()


@dp.message_handler(text_startswith='ch')
async def check_ban(message: Message):
    await message.answer('The message has been processed, you are not blocked.')


@dp.message_handler(commands=['s', 'session'])
async def session_check(message: Message, session: ExampleDatabase):
    session.set('name', 'Marina')
    session.set('age', '21')
    await message.answer('Hello man!')


async def handler_gupshup(request):
    event = await request.json()
    await dp.handle_event(event)
    return web.Response(status=200)


if __name__ == "__main__":
    webhook.add_routes([web.post('/api/v1/gupshup/hook', handler_gupshup)])
    web.run_app(webhook, port=8017)
```
<br>

#### An example of using middleware in our github:
<a href="https://github.com/dotX12/waio/tree/master/examples/middleware">Middleware example</a>
