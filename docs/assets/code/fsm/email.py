@dp.message_handler(state=RegisterStates.birthday)
async def register_age(message: Message, state: FSMContext):
    await state.set_data(birthday=message.text)
    await message.answer(f'Thanks for sending you birthday!\n'
                         f'Send you email address')
    await state.set_state(RegisterStates.email)
