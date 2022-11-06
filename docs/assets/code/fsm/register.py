@dp.message_handler(commands=["register"], state="*")
async def register_name(event: Event, state: FSMContext):
    await event.answer(f"Hi, {event.sender_name}! send your date of birth")
    await state.set_state(RegisterStates.birthday)
