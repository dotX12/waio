from aiohttp import web

from examples.routers.binding import own_router
from examples.routers.middlewares import BanMiddleware
from waio import Bot
from waio import Dispatcher
from waio.logs import loguru_filter

loguru_filter.set_level("DEBUG")

bot = Bot(
    apikey="",
    src_name="",
    phone_number=917834811114,
)


dp = Dispatcher(bot=bot, name="Dispatcher")
dp.labeler.register_middleware(BanMiddleware())
dp.include_router(own_router)


async def handler_gupshup(request):
    event = await request.json()
    await dp.handle_event(event)
    return web.Response(status=200)


if __name__ == "__main__":
    webhook = web.Application()
    webhook.add_routes([web.post("/api/v1/gupshup/hook", handler_gupshup)])
    web.run_app(webhook, port=8005)
