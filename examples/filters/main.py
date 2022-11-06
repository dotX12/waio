import re

from aiohttp import web

from examples.filters.rule_long_message import LongMessageRule
from examples.filters.rule_number import RussianNumberRule
from waio.bot import Bot
from waio.dispatcher.dispatcher import Dispatcher
from waio.logs import loguru_filter
from waio.rules import MessageCommandsRule
from waio.rules import TextRule
from waio.types import ContentType
from waio.types import Event
from waio import F

loguru_filter.set_level("DEBUG")

bot = Bot(
    apikey="",
    src_name="",
    phone_number=917834811114,
)

dp = Dispatcher(bot=bot)
dp.labeler.bind_rule("len", LongMessageRule)


@dp.message_handler(RussianNumberRule(), commands=["check_number"])
async def text_rule_check_number(event: Event, number_data):
    await event.answer(f"You are from Russia! Number data:\n```{number_data}```")


@dp.message_handler(commands=["start", "echo"], content_type=[ContentType.TEXT])
async def start_commands(event):
    await event.answer(
        f"Filter used: [commands and content_type:TEXT], msg: {event.message.payload.text}"
    )


@dp.message_handler(content_type=[ContentType.PHOTO])
async def start_photo(event: Event):
    await event.answer(
        f"Filter used: [content_type:PHOTO], url_photo: {event.message.payload.url}"
    )


@dp.message_handler(regex=r"cart_id_(?P<cart_id>\d+)_item_id_(?P<item_id>\d+)$")
async def start_regex(event: Event, regex: re.Match):
    cart_id = regex.group("cart_id")
    item_id = regex.group("item_id")
    await event.answer(f"Filter used: [regex], cart_id: {cart_id}, item_id: {item_id}")


@dp.message_handler(text_equals=["foo", "bar"])
async def start_text_equals(event: Event):
    await event.answer(f"Filter used: [text_equals], msg: {event.text}")


@dp.message_handler(text_contains=["ru", "com"])
async def start_text_contains(event: Event):
    await event.answer(f"Filter used: [text_contains], msg: {event.text}")


@dp.message_handler(text_startswith=["ftp", "sftp"])
async def text_startswith(event: Event):
    await event.answer(f"Filter used: [text_startswith], msg: {event.text}")


@dp.message_handler(text_endswith=[".png", ".jpg"])
async def text_endswith(event: Event):
    await event.answer(f"Filter used: [text_endswith], msg: {event.text}")


@dp.message_handler(LongMessageRule(len_message=100))
async def text_len(event: Event):
    await event.answer(f"Filter used: [LongMessageRule], msg_len: {len(event.text)}")


@dp.message_handler(len=12)
async def text_len(event: Event):
    await event.answer(
        f"Filter used: [labeler: len = LongMessageRule], msg_len: {len(event.text)}"
    )


@dp.message_handler(MessageCommandsRule(commands=["start", "echo"]))
async def commands_rule_without_labeler(event: Event):
    await event.answer(f"Filter used: [MessageCommandsRule], msg: {event.text}")


@dp.message_handler(
    TextRule(startswith=["1111", "2222"], endswith=["x", "y", "z"]),
    content_type=[ContentType.TEXT],
)
async def text_start_switch_without_labeler(event: Event):
    await event.answer(f"Filter used: [TextRule], msg: {event.text}")


@dp.message_handler(
    (F.message.payload.content_type == "image/gif")
    & (F.message.payload.sender.name == "Alex")
    & ((F.message.payload.sender.phone.cast(str)[:4]) == '7928')
)
async def test_magic_filter(event: Event):
    await event.answer(
        f"Test Filter"
    )


async def handler_gupshup(request):
    event = await request.json()
    await dp.handle_event(event)
    return web.Response(status=200)


if __name__ == "__main__":
    webhook = web.Application()
    webhook.add_routes([web.post("/api/v1/gupshup/hook", handler_gupshup)])
    web.run_app(webhook, port=8005)
