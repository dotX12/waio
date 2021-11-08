from waio.rules import ABCRule


class DynamicLongMessageRule(ABCRule):
    def __init__(self, len_message: int):
        self.len_message = len_message

    async def check(self, message: Message) -> bool:
        return len(message.text) > self.len_message

