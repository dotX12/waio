@dp.message_handler()
async def start_switch(message: Message):
    await message.answer(f'Hello, {message.message.payload.sender.name},'
                         f' text: {message.message.payload.text}')