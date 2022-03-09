import asyncio
from aiohttp import web

from examples.list_keyboard.callbacks import callback_element_rice
from waio import Bot, Dispatcher
from waio.logs import loguru_filter
from waio.types import Message
from examples.list_keyboard.button import generate_button
from examples.list_keyboard.callbacks import callback_element_potato

loguru_filter.set_level('DEBUG')

bot = Bot(
    apikey='',
    src_name='',
    phone_number=1337
)

dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["dinner"])
async def start(message: Message):
    await bot.send_list(
        receiver=message.sender_number,
        keyboard=generate_button()
    )


@dp.message_handler(callback_element_potato.filter(id=["1", "2"]))
async def mashed_potatoes(message: Message):
    if message.callback_data_item.endswith("1"):
        await message.answer("Отличный выбор! Сегодня на ужин у Вас пюре с котлетками")
    if message.callback_data_item.endswith("2"):
        await message.answer("Отличный выбор! Сегодня на ужин у Вас пюре с курочкой")


# OR
# dp.register_message_handler(
#     handler=mashed_potatoes,
#     callback=callback_element_potato.filter(id=["1", "2"]),
# )

# Пример отлова колбеков с фильтром и обработка по аргументам
@dp.message_handler(callback_element_rice.filter())
async def rice(message: Message):
    if message.callback_data_item.split(sep=":")[1] == "cutlets":  # Обработка по name
        await message.answer(f"Отличный выбор! Сегодня на ужин у Вас рис с котлетками")
    if message.callback_data_item.split(sep=":")[1] == "chicken":
        await message.answer("Отличный выбор! Сегодня на ужин у Вас рис с курочкой")


async def handler_gupshup(request):
    event = await request.json()
    await dp.handle_event(event)
    return web.Response(status=200)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    webhook = web.Application()
    webhook.add_routes([web.post('/api/v1/gupshup/hook', handler_gupshup)])
    web.run_app(webhook, port=8017)
