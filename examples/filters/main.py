import re

from aiohttp import web
from waio import Bot, Dispatcher
from waio.types import Message, ContentType
from waio.logs import loguru_filter
from waio.rules import TextRule, MessageCommandsRule

from examples.filters.rule_long_message import LongMessageRule
from examples.filters.rule_number import RussianNumberRule

loguru_filter.set_level('DEBUG')

bot = Bot(
    apikey='API_KEY',
    src_name='SRC_NAME',
    phone_number=79289998877
)

dp = Dispatcher(bot=bot)

dp.labeler.bind_rule('len', LongMessageRule)


@dp.message_handler(RussianNumberRule(), commands=["check_number"])
async def text_rule_check_number(message: Message, number_data):
    await message.answer(f'You are from Russia! Number data:\n```{number_data}```')


@dp.message_handler(commands=['start', 'echo'], content_type=[ContentType.TEXT])
async def start_commands(message: Message):
    await message.answer(f'Filter used: [commands and content_type:TEXT], msg: {message.message.payload.text}')


@dp.message_handler(content_type=[ContentType.PHOTO])
async def start_photo(message: Message):
    await message.answer(f'Filter used: [content_type:PHOTO], url_photo: {message.message.payload.url}')


@dp.message_handler(regex=r'cart_id_(?P<cart_id>\d+)_item_id_(?P<item_id>\d+)$')
async def start_regex(message: Message, regex: re.Match):
    cart_id = regex.group('cart_id')
    item_id = regex.group('item_id')
    await message.answer(f'Filter used: [regex], cart_id: {cart_id}, item_id: {item_id}')


@dp.message_handler(text_equals=['foo', 'bar'])
async def start_text_equals(message: Message):
    await message.answer(f'Filter used: [text_equals], msg: {message.text}')


@dp.message_handler(text_contains=['ru', 'com'])
async def start_text_contains(message: Message):
    await message.answer(f'Filter used: [text_contains], msg: {message.text}')


@dp.message_handler(text_startswith=['ftp', 'sftp'])
async def text_startswith(message: Message):
    await message.answer(f'Filter used: [text_startswith], msg: {message.text}')


@dp.message_handler(text_endswith=['.png', '.jpg'])
async def text_endswith(message: Message):
    await message.answer(f'Filter used: [text_endswith], msg: {message.text}')


@dp.message_handler(LongMessageRule(len_message=100))
async def text_len(message: Message):
    await message.answer(f'Filter used: [LongMessageRule], msg_len: {len(message.text)}')


@dp.message_handler(len=12)
async def text_len(message: Message):
    await message.answer(f'Filter used: [labeler: len = LongMessageRule], msg_len: {len(message.text)}')


@dp.message_handler(MessageCommandsRule(commands=['start', 'echo']))
async def commands_rule_without_labeler(message: Message):
    await message.answer(f'Filter used: [MessageCommandsRule], msg: {message.text}')


@dp.message_handler(
    TextRule(startswith=['1111', '2222'], endswith=['x', 'y', 'z']), content_type=[ContentType.TEXT])
async def text_start_switch_without_labeler(message: Message):
    await message.answer(f'Filter used: [TextRule], msg: {message.text}')


async def handler_gupshup(request):
    event = await request.json()
    await dp.handle_event(event)
    return web.Response(status=200)


if __name__ == "__main__":
    webhook = web.Application()
    webhook.add_routes([web.post('/api/v1/gupshup/hook', handler_gupshup)])
    web.run_app(webhook, port=8017)
