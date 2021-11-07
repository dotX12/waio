from aiohttp import web

from examples.middleware.database import ExampleDatabase
from waio.types import Message
from misc import *

webhook = web.Application()


@dp.message_handler(text_startswith='ch')
async def check_ban(message: Message):
    await message.answer('The message has been processed, you are not blocked.')


@dp.message_handler(commands=['s', 'session'])
async def session_check(message: Message, session: ExampleDatabase):
    session.set('name', 'Marina')
    session.set('age', '21')
    await message.answer('Hello man!')


async def handler_gupshup(request):
    event = await request.json()
    await dp.handle_event(event)
    return web.Response(status=200)


if __name__ == "__main__":
    webhook.add_routes([web.post('/api/v1/gupshup/hook', handler_gupshup)])
    web.run_app(webhook, port=8017)
