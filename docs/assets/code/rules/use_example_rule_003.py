@dp.message_handler(len_more=12)
async def text_len(message: Message):
    await message.answer(f'msg len: {len(message.text)}')