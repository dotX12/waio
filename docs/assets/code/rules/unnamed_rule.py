from waio.rules import MessageCommandsRule


@dp.message_handler(MessageCommandsRule(commands=["start", "echo"]))
async def commands_rule_without_labeler(event: Event):
    await event.answer(f"Filter used: [MessageCommandsRule], msg: {event.text}")
