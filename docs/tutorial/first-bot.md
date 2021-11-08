## Simple template
At first you have to import all necessary modules.

```python3
from aiohttp import web
from waio import Bot, Dispatcher
from waio.types import Message
from waio.logs import loguru_filter
```

Then you have to initialize bot and dispatcher instances.
src_name, phone_number, apikey can be obtained from your gupshup account.

```python3
loguru_filter.set_level('DEBUG')

bot = Bot(
    apikey='algAJW9512kMWGALZIkAMWG',
    src_name='test_client18215',
    phone_number='79189998877'
)

dp = Dispatcher(bot=bot)
```

Next step: interaction with bots starts with one command.
Register your first command handler:

```python3
@dp.message_handler(commands=['start', 'echo'])
async def start_command(message: Message):
    """
    This handler will be called when user sends
    `/start` or `/echo` command
    """
    await message.answer(f'Hello, {message.message.payload.sender.name}')
```
If you want to handle all text messages in the chat simply add handler without filters:
```python3
@dp.message_handler()
async def start_switch(message: Message):
    await message.answer(f'Hello, {message.message.payload.sender.name}, text: {message.message.payload.text}')
```

Last step: run webhook.

```python3
async def handler_gupshup(request):
    event = await request.json()
    await dp.handle_event(event)
    return web.Response(status=200)


if __name__ == "__main__":
    webhook = web.Application()
    webhook.add_routes([web.post('/api/v1/gupshup/hook', handler_gupshup)])
    web.run_app(webhook, port=8017)
```

### Summary

```python3
from aiohttp import web
from waio import Bot, Dispatcher
from waio.types import Message
from waio.logs import loguru_filter

loguru_filter.set_level('DEBUG')

bot = Bot(
    apikey='algAJW9512kMWGALZIkAMWG',
    src_name='test_client18215',
    phone_number='79189998877'
)

dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start', 'echo'])
async def start_command(message: Message):
    """
    This handler will be called when user sends
    `/start` or `/echo` command
    """
    await message.answer(f'Hello, {message.message.payload.sender.name}')


@dp.message_handler(text_startswitch=['!!', '##'])
async def start_switch(message: Message):
    await message.answer(f'Hello, {message.message.payload.sender.name}, text: {message.message.payload.text}')


async def handler_gupshup(request):
    event = await request.json()
    await dp.handle_event(event)
    return web.Response(status=200)


if __name__ == "__main__":
    webhook = web.Application()
    webhook.add_routes([web.post('/api/v1/gupshup/hook', handler_gupshup)])
    web.run_app(webhook, port=8017)
```