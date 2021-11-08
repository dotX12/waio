from aiohttp import web

from waio import Bot, Dispatcher
from waio.rules.abc import ABCRule
from waio.types import Message
from waio.logs import loguru_filter

loguru_filter.set_level('DEBUG')

bot = Bot(
    apikey='API_KEY',
    src_name='SRC_NAME',
    phone_number=79281112233
)

dp = Dispatcher(bot=bot)


class DynamicLongMessageRule(ABCRule):
    def __init__(self, len_message: int):
        self.len_message = len_message

    async def check(self, message: Message) -> bool:
        return len(message.text) > self.len_message


dp.labeler.bind_rule('len_more', DynamicLongMessageRule)


@dp.message_handler(len_more=20)
async def text_len(message: Message):
    await message.answer(f'msg len: {len(message.text)}')


async def handler_gupshup(request):
    event = await request.json()
    await dp.handle_event(event)
    return web.Response(status=200)


if __name__ == "__main__":
    webhook = web.Application()
    webhook.add_routes([web.post('/api/v1/gupshup/hook', handler_gupshup)])
    web.run_app(webhook, port=8017)
