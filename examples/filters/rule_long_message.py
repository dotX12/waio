from waio.rules import ABCRule
from waio.types import Message


class LongMessageRule(ABCRule):
    def __init__(self, len_message: int):
        self.len_message = len_message

    async def check(self, message: Message) -> bool:
        return len(message.text) > self.len_message
