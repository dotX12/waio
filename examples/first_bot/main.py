from aiohttp import web

from waio import Bot, Dispatcher
from waio.types import Event
from waio.logs import loguru_filter

loguru_filter.set_level("DEBUG")

bot = Bot(apikey="API_KEY", src_name="SRC_NAME", phone_number=0000000000)

dp = Dispatcher(bot=bot)


# router = Router()


@dp.message_handler(commands=["start", "echo"])
async def start_command(event: Event):
    """
    This handler will be called when user sends
    `/start` or `/echo` command
    """
    await event.answer(f"Hello, {event.message.payload.sender.name}")


@dp.message_handler(text_startswitch=["!!", "##"])
async def start_switch(event: Event):
    await event.answer(
        f"Hello, {event.message.payload.sender.name},"
        f" text: {event.message.payload.text}"
    )


async def handler_gupshup(request):
    event = await request.json()
    await dp.handle_event(event)
    return web.Response(status=200)


if __name__ == "__main__":
    webhook = web.Application()
    webhook.add_routes([web.post("/api/v1/gupshup/hook", handler_gupshup)])
    web.run_app(webhook, port=8017)
