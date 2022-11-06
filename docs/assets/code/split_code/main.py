from aiohttp import web
from waio.types import ContentType

from misc import dp, webhook
from handlers_foo import start_commands, start_photo, start_regex, start_text_equals

dp.register_message_handler(
    handler=start_commands, commands=["start", "echo"], content_type=[ContentType.TEXT]
)

dp.register_message_handler(handler=start_photo, content_type=[ContentType.PHOTO])
dp.register_message_handler(
    handler=start_regex, regex=r"cart_id_(?P<cart_id>\d+)_item_id_(?P<item_id>\d+)$"
)
dp.register_message_handler(handler=start_text_equals, text_equals=["foo", "bar"])


async def handler_gupshup(request):
    event = await request.json()
    await dp.handle_event(event)
    return web.Response(status=200)


if __name__ == "__main__":
    webhook.add_routes([web.post("/api/v1/gupshup/hook", handler_gupshup)])
    web.run_app(webhook, port=8017)
