import asyncio
from aiohttp import web
from waio.rules import ABCRule
from waio import Bot, Dispatcher
from waio.logs import loguru_filter
from waio.types import Message
from waio.rules import TextRule, ContentType, PrefixRule
from examples.list_keyboard.button import generate_button
from examples.list_keyboard.callbacks import callback_element_potato, callback_list_dish, callback_element_rice

# Some code...


@dp.message_handler(commands=["dinner"])
async def start(message: Message):
    await bot.send_list(receiver=message.sender_number, button=generate_button())


# Пример отлова колбеков по id
@dp.message_handler(callback_element_potato.filter(id=["1", "2"]))
async def mashed_potatoes(message: Message):
    if message.callback_data_item.endswith("1"):
        await message.answer("Отличный выбор! Сегодня на ужин у Вас пюре с котлетками")
    if message.callback_data_item.endswith("2"):
        await message.answer("Отличный выбор! Сегодня на ужин у Вас пюре с курочкой")


# Пример отлова колбеков с фильтром и обработка по аргументам
@dp.message_handler(callback_element_rice.filter())
async def rice(message: Message):
    if message.callback_data_item.split(sep=":")[1] == "cutlets":  # Обработка name
        await message.answer(f"Отличный выбор! Сегодня на ужин у Вас рис с котлетками")
    if message.callback_data_item.split(sep=":")[1] == "chicken":
        await message.answer("Отличный выбор! Сегодня на ужин у Вас рис с курочкой")