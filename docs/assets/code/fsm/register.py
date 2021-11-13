@dp.message_handler(commands=['register'], state='*')
async def register_name(message: Message, state: FSMContext):
    await message.answer(f'Hi, {message.sender_name}! send your date of birth')
    await state.set_state(RegisterStates.birthday)
