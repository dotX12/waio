from re import Match

from waio.types import Event


async def start_commands(event: Event):
    await event.answer(
        f"Filter used: [commands and content_type:TEXT], "
        f"msg: {event.message.payload.text}"
    )


async def start_photo(event: Event):
    await event.answer(
        f"Filter used: [content_type:PHOTO], " f"url_photo: {event.message.payload.url}"
    )


async def start_regex(event: Event, regex: Match):
    cart_id = regex.group("cart_id")
    item_id = regex.group("item_id")
    await event.answer(
        f"Filter used: [regex], " f"cart_id: {cart_id}, item_id: {item_id}"
    )


async def start_text_equals(event: Event):
    await event.answer(f"Filter used: [text_equals], " f"msg: {event.text}")
