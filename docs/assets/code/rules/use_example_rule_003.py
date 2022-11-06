@dp.message_handler(len_more=12)
async def text_len(event: Event):
    await event.answer(f"msg len: {len(event.text)}")
