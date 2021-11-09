import asyncio
from typing import Dict
from aiohttp import web

from examples.reply_keyboard.button import generate_keyboard
from examples.reply_keyboard.callback import callback_reply_keyboard
from waio import Bot, Dispatcher
from waio.logs import loguru_filter
from waio.types import Message

loguru_filter.set_level('DEBUG')

bot = Bot(
    apikey='API_KEY',
    src_name='SRC_NAME',
    phone_number=000000000
)

dp = Dispatcher(bot=bot)


@dp.message_handler(callback_reply_keyboard.filter(type='start'))
async def start_command(message: Message, callback_data: Dict):
    await message.answer(f'Triggered Reply Keyboard\n'
                         f'Message: {message.message}\n'
                         f'CallbackData: {callback_data}')


async def handler_gupshup(request):
    event = await request.json()
    await dp.handle_event(event)
    return web.Response(status=200)


async def _send_keyboard():
    await bot.send_list(receiver=79109998877, button=generate_keyboard())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_send_keyboard())

    webhook = web.Application()
    webhook.add_routes([web.post('/api/v1/gupshup/hook', handler_gupshup)])
    web.run_app(webhook, port=8017)
