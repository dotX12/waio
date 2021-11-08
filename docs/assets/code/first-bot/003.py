@dp.message_handler(commands=['start', 'echo'])
async def start_command(message: Message):
    """
    This handler will be called when user sends
    `/start` or `/echo` command
    """
    await message.answer(f'Hello, {message.message.payload.sender.name}')