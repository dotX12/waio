@dp.message_handler()
async def start_switch(event: Event):
    await event.answer(
        f"Hello, {event.message.payload.sender.name},"
        f" text: {event.message.payload.text}"
    )
