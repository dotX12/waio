from aiohttp import web

from waio import Bot, Dispatcher
from waio.logs import loguru_filter
from waio.types import Message

loguru_filter.set_level('DEBUG')

bot = Bot(
    apikey='API_KEY',
    src_name='SRC_NAME',
    phone_number=0000000000
)

dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    await message.bot.send_video(
        receiver=message.sender_number,
        url="https://www.buildquickbots.com/whatsapp/media/sample/video/sample01.mp4",
        caption="Test video caption"
    )


async def handler_gupshup(request):
    event = await request.json()
    await dp.handle_event(event)
    return web.Response(status=200)


if __name__ == "__main__":
    webhook = web.Application()
    webhook.add_routes([web.post('/api/v1/gupshup/hook', handler_gupshup)])
    web.run_app(webhook, port=8008)
