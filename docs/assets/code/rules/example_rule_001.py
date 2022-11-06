from waio.rules import ABCRule
from waio.types import Event


class StaticLongMessageRule(ABCRule):
    async def check(self, event: Event) -> bool:
        return len(event.text) > 200
