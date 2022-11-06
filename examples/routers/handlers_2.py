from waio import Router
from waio.types import Event


router2 = Router(name='Router2')


@router2.message_handler(commands=['start'])
async def text_start(event: Event):
    await event.answer("started...")

