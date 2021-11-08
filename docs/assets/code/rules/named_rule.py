@dp.message_handler(text_equals=['foo', 'bar'])
async def start_text_equals(message: Message):
    await message.answer(f'Filter used: [text_equals], msg: {message.text}')


@dp.message_handler(text_contains=['ru', 'com'])
async def start_text_contains(message: Message):
    await message.answer(f'Filter used: [text_contains], msg: {message.text}')