@dp.message_handler(RussianNumberRule(), commands=["check_number"])
async def register_rule_check_number(message: Message, number_data: G_T):
    await message.answer(
        f'You are from Russia! Number data:\n'
        f'```{number_data}```'
    )
