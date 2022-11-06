@dp.message_handler(state=RegisterStates.birthday)
async def register_age(event: Event, state: FSMContext):
    await state.set_data(birthday=event.text)
    await event.answer(f"Thanks for sending you birthday!\n" f"Send you email address")
    await state.set_state(RegisterStates.email)
