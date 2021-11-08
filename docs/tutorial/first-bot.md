[comment]: <> (## Simple template)

[comment]: <> (At first you have to import all necessary modules.)

[comment]: <> (```python3)

[comment]: <> (from aiohttp import web)

[comment]: <> (from waio import Bot, Dispatcher)

[comment]: <> (from waio.types import Message)

[comment]: <> (from waio.logs import loguru_filter)

[comment]: <> (```)

[comment]: <> (Then you have to initialize bot and dispatcher instances.)

[comment]: <> (src_name, phone_number, apikey can be obtained from your gupshup account.)

[comment]: <> (```python3)

[comment]: <> (loguru_filter.set_level&#40;'DEBUG'&#41;)

[comment]: <> (bot = Bot&#40;)

[comment]: <> (    apikey='algAJW9512kMWGALZIkAMWG',)

[comment]: <> (    src_name='test_client18215',)

[comment]: <> (    phone_number='79189998877')

[comment]: <> (&#41;)

[comment]: <> (dp = Dispatcher&#40;bot=bot&#41;)

[comment]: <> (```)

[comment]: <> (Next step: interaction with bots starts with one command.)

[comment]: <> (Register your first command handler:)

[comment]: <> (```python3)

[comment]: <> (@dp.message_handler&#40;commands=['start', 'echo']&#41;)

[comment]: <> (async def start_command&#40;message: Message&#41;:)

[comment]: <> (    """)

[comment]: <> (    This handler will be called when user sends)

[comment]: <> (    `/start` or `/echo` command)

[comment]: <> (    """)

[comment]: <> (    await message.answer&#40;f'Hello, {message.message.payload.sender.name}'&#41;)

[comment]: <> (```)

[comment]: <> (If you want to handle all text messages in the chat simply add handler without filters:)

[comment]: <> (```python3)

[comment]: <> (@dp.message_handler&#40;&#41;)

[comment]: <> (async def start_switch&#40;message: Message&#41;:)

[comment]: <> (    await message.answer&#40;f'Hello, {message.message.payload.sender.name},')

[comment]: <> (                         f' text: {message.message.payload.text}'&#41;)

[comment]: <> (```)

[comment]: <> (Last step: run webhook.)

[comment]: <> (```python3)

[comment]: <> (async def handler_gupshup&#40;request&#41;:)

[comment]: <> (    event = await request.json&#40;&#41;)

[comment]: <> (    await dp.handle_event&#40;event&#41;)

[comment]: <> (    return web.Response&#40;status=200&#41;)


[comment]: <> (if __name__ == "__main__":)

[comment]: <> (    webhook = web.Application&#40;&#41;)

[comment]: <> (    webhook.add_routes&#40;[web.post&#40;'/api/v1/gupshup/hook', handler_gupshup&#41;]&#41;)

[comment]: <> (    web.run_app&#40;webhook, port=8017&#41;)

[comment]: <> (```)

[comment]: <> (### Summary)

[comment]: <> (```python3)

[comment]: <> (from aiohttp import web)

[comment]: <> (from waio import Bot, Dispatcher)

[comment]: <> (from waio.types import Message)

[comment]: <> (from waio.logs import loguru_filter)

[comment]: <> (loguru_filter.set_level&#40;'DEBUG'&#41;)

[comment]: <> (bot = Bot&#40;)

[comment]: <> (    apikey='algAJW9512kMWGALZIkAMWG',)

[comment]: <> (    src_name='test_client18215',)

[comment]: <> (    phone_number='79189998877')

[comment]: <> (&#41;)

[comment]: <> (dp = Dispatcher&#40;bot=bot&#41;)


[comment]: <> (@dp.message_handler&#40;commands=['start', 'echo']&#41;)

[comment]: <> (async def start_command&#40;message: Message&#41;:)

[comment]: <> (    """)

[comment]: <> (    This handler will be called when user sends)

[comment]: <> (    `/start` or `/echo` command)

[comment]: <> (    """)

[comment]: <> (    await message.answer&#40;f'Hello, {message.message.payload.sender.name}'&#41;)


[comment]: <> (@dp.message_handler&#40;text_startswitch=['!!', '##']&#41;)

[comment]: <> (async def start_switch&#40;message: Message&#41;:)

[comment]: <> (    await message.answer&#40;f'Hello, {message.message.payload.sender.name},')

[comment]: <> (                         f' text: {message.message.payload.text}'&#41;)

[comment]: <> (async def handler_gupshup&#40;request&#41;:)

[comment]: <> (    event = await request.json&#40;&#41;)

[comment]: <> (    await dp.handle_event&#40;event&#41;)

[comment]: <> (    return web.Response&#40;status=200&#41;)


[comment]: <> (if __name__ == "__main__":)

[comment]: <> (    webhook = web.Application&#40;&#41;)

[comment]: <> (    webhook.add_routes&#40;[web.post&#40;'/api/v1/gupshup/hook', handler_gupshup&#41;]&#41;)

[comment]: <> (    web.run_app&#40;webhook, port=8017&#41;)

[comment]: <> (```)