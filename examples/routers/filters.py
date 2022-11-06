from waio.rules import ABCRule
from waio.types import Event


class DynamicLongMessageRule(ABCRule):

    def __init__(self, len_message: int):
        self.len_message = len_message

    async def check(self, event: Event) -> bool:
        return len(event.text) > self.len_message
