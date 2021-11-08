from waio.rules import TextRule, ContentType


@dp.message_handler(
    TextRule(startswith=['1111', '2222'], endswith=['x', 'y', 'z']),
    content_type=[ContentType.TEXT]
)
async def text_start_switch_without_labeler(message: Message):
    await message.answer(f'Filter used: [TextRule], msg: {message.text}')