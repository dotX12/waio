@dp.message_handler(text_equals=["foo", "bar"])
async def start_text_equals(event: Event):
    await event.answer(f"Filter used: [text_equals], msg: {event.text}")


@dp.message_handler(text_contains=["ru", "com"])
async def start_text_contains(event: Event):
    await event.answer(f"Filter used: [text_contains], msg: {event.text}")
