import asyncio
from aiohttp import web

from waio import Bot, Dispatcher
from waio.logs import loguru_filter
from waio.types import Message
from examples.list_keyboard.button import generate_button
from examples.list_keyboard.callbacks import callback_element_restaurant, callback_list_restaurant

loguru_filter.set_level('DEBUG')

bot = Bot(
    apikey='API_KEY',
    src_name='SRC_NAME',
    phone_number=00000000)

dp = Dispatcher(bot=bot)


@dp.message_handler(callback_element_restaurant.filter(name='kfc'))
async def start_command(message: Message):
    await message.answer(f'Triggered on: callback_element_restaurant [KFC]\n'
                         f'CallbackDataList: {message.callback_data_list}\n'
                         f'CallbackDataItem: {message.callback_data_item}\n')


@dp.message_handler(callback_list_restaurant.filter(id='1337'))
async def start_command(message: Message):
    await message.answer(f'Triggered on callback_list_restaurant\n'
                         f'CallbackDataList: {message.callback_data_list}\n'
                         f'CallbackDataItem: {message.callback_data_item}\n')


async def handler_gupshup(request):
    event = await request.json()
    await dp.handle_event(event)
    return web.Response(status=200)


async def _send_keyboard():
    await bot.send_list(receiver=79109998877, button=generate_button())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_send_keyboard())

    webhook = web.Application()
    webhook.add_routes([web.post('/api/v1/gupshup/hook', handler_gupshup)])
    web.run_app(webhook, port=8017)
