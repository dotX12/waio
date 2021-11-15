from typing import Dict
from aiohttp import web
from aiohttp.web_request import Request

from examples.reply_keyboard.button import generate_keyboard_place, generate_keyboard_image, \
    generate_keyboard_restaurant_time, generate_keyboard_cinema_time
from examples.reply_keyboard.callback import callback_reply_keyboard
from waio import Bot, Dispatcher
from waio.logs import loguru_filter
from waio.types import Message

from settings import apikey, src_name, phone_number

loguru_filter.set_level('DEBUG')

bot = Bot(
    apikey=apikey,
    src_name=src_name,
    phone_number=phone_number
)

dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['place'])  # Обработчик команды /place
async def place(message: Message):
    await message.bot.send_reply(receiver=message.sender_number, keyboard=generate_keyboard_place())


@dp.message_handler(callback_reply_keyboard.filter(name="place"))  # Обработчик колбэка выбранного места
async def place_choose(message: Message, callback_data: Dict):
    if message.message.payload.title == "Кинотеатр":  # Обработка по тексту сообщения
        await message.bot.send_reply(receiver=message.sender_number, keyboard=generate_keyboard_cinema_time())
    if message.message.payload.title == "Ресторан":
        await message.bot.send_reply(receiver=message.sender_number, keyboard=generate_keyboard_restaurant_time())


@dp.message_handler(callback_reply_keyboard.filter(name="cinema_time"))  # Обработчик колбэка выбора времени для кино
async def cinema_time(message: Message, callback_data: Dict):
    await message.answer(f"Отлично! Вы записаны в кинотеатр на {message.message.payload.title}")


@dp.message_handler(callback_reply_keyboard.filter(name="restaurant_time"))  # Обработчик колбэка выбора времени для ресторана
async def rest_time(message: Message, callback_data: Dict):
    await message.answer(f"Отлично! Вы записаны в ресторан на {message.message.payload.title}")


async def handler_gupshup(request: Request):
    event = await request.json()
    await dp.handle_event(event)
    return web.Response(status=200)


if __name__ == "__main__":
    webhook = web.Application()
    webhook.add_routes([web.post('/api/v1/gupshup/hook', handler_gupshup)])
    web.run_app(webhook, port=8017)
