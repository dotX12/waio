@dp.message_handler(commands=["start", "echo"])
async def start_command(event: Event):
    """
    This handler will be called when user sends
    `/start` or `/echo` command
    """
    await event.answer(f"Hello, {event.message.payload.sender.name}")
