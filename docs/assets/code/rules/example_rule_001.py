from waio.rules import ABCRule


class StaticLongMessageRule(ABCRule):
    async def check(self, message: Message) -> bool:
        return len(message.text) > 200
