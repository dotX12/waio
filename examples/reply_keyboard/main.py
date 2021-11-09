from typing import Dict

from aiohttp import web
from aiohttp.web_request import Request
from waio import Bot, Dispatcher
from waio.logs import loguru_filter
from waio.types import Message


from examples.reply_keyboard.button import generate_keyboard
from examples.reply_keyboard.callback import callback_reply_keyboard
loguru_filter.set_level('DEBUG')

bot = Bot(
    apikey='API_KEY',
    src_name='SRC_NAME',
    phone_number=0000000000
)

dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['keyboard'])
async def get_keyboard(message: Message):
    await message.bot.send_reply(receiver=message.sender_number, keyboard=generate_keyboard())


@dp.message_handler(callback_reply_keyboard.filter(type='start'))
async def start_command(message: Message, callback_data: Dict):
    await message.answer(f'Triggered Reply Keyboard\n'
                         f'Message: {message.message}\n'
                         f'CallbackData: {callback_data}')


async def handler_gupshup(request: Request):
    event = await request.json()
    await dp.handle_event(event)
    return web.Response(status=200)


if __name__ == "__main__":
    webhook = web.Application()
    webhook.add_routes([web.post('/api/v1/gupshup/hook', handler_gupshup)])
    web.run_app(webhook, port=8017)
