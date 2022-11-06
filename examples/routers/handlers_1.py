from examples.routers.filters import DynamicLongMessageRule
from waio import Router
from waio.types import Event

router1 = Router(name='Router 1')
router1.labeler.bind_rule("len_more", DynamicLongMessageRule)


@router1.message_handler(len_more=20)
async def text_len(event: Event):
    await event.answer(f"msg len: {len(event.text)}")

