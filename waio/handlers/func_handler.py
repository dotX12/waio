from typing import Callable, Union, Any
from waio.rules.abc import ABCRule


class FromFuncHandler:
    def __init__(self, handler: Callable, *rules: ABCRule):
        self.handler = handler
        self.rules = rules

    async def filter(self, event: Any) -> Union[dict, bool]:
        rule_context = {}
        for rule in self.rules:
            result = await rule.check(event)
            if result is False or result is None:
                return False
            elif result is True:
                continue
            rule_context.update(result)
        return rule_context

    async def handle(self, **context) -> Any:
        return await self.handler(**context)

    def __repr__(self):
        return (
            f"<FromFuncHandler {self.handler.__name__} "
            f"rules={self.rules}>"
        )
