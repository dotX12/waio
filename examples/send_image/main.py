from aiohttp import web

from waio import Bot, Dispatcher
from waio.types import Event
from waio.logs import loguru_filter

loguru_filter.set_level("DEBUG")

bot = Bot(apikey="test", src_name="test", phone_number=0000000000000)

dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def start_command(event: Event):
    await event.bot.send_image(
        receiver=event.sender_number,
        original_url="https://www.buildquickbots.com/whatsapp/media"
        "/sample/jpg/sample01.jpg",
        caption="Test caption",
    )


async def handler_gupshup(request):
    event = await request.json()
    await dp.handle_event(event)
    return web.Response(status=200)


if __name__ == "__main__":
    webhook = web.Application()
    webhook.add_routes([web.post("/api/v1/gupshup/hook", handler_gupshup)])
    web.run_app(webhook, port=8008)
