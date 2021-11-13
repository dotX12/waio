from re import Match

from waio.types import Message


async def start_commands(message: Message):
    await message.answer(
        f'Filter used: [commands and content_type:TEXT], '
        f'msg: {message.message.payload.text}'
    )


async def start_photo(message: Message):
    await message.answer(
        f'Filter used: [content_type:PHOTO], '
        f'url_photo: {message.message.payload.url}'
    )


async def start_regex(message: Message, regex: Match):
    cart_id = regex.group('cart_id')
    item_id = regex.group('item_id')
    await message.answer(
        f'Filter used: [regex], '
        f'cart_id: {cart_id}, item_id: {item_id}'
    )


async def start_text_equals(message: Message):
    await message.answer(
        f'Filter used: [text_equals], '
        f'msg: {message.text}'
    )
