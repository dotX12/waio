from waio.rules import TextRule, ContentType
from waio.types import Event


@dp.message_handler(
    TextRule(startswith=["1111", "2222"], endswith=["x", "y", "z"]),
    content_type=[ContentType.TEXT],
)
async def text_start_switch_without_labeler(event: Event):
    await event.answer(f"Filter used: [TextRule], msg: {event.text}")
