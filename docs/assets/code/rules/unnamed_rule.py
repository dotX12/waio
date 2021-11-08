from waio.rules import MessageCommandsRule

@dp.message_handler(MessageCommandsRule(commands=['start', 'echo']))
async def commands_rule_without_labeler(message: Message):
    await message.answer(
        f'Filter used: [MessageCommandsRule], msg: {message.text}'
    )
