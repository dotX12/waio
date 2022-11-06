from typing import Callable, Union, Any
from typing import Dict

from magic_filter import MagicFilter

from waio.rules.abc import ABCRule
from waio.types import Event


class FromFuncHandler:
    def __init__(self, handler: Callable, *rules: ABCRule):
        self.handler = handler
        self.rules = rules

    @classmethod
    async def _f_rule_event(
        cls,
        rule: Union[ABCRule, MagicFilter],
        event: Event
    ) -> Union[bool, Dict[Any, Any]]:
        if isinstance(rule, MagicFilter):
            result = rule.resolve(event)
            return result
        return await rule.check(event)

    async def filter(self, event: Event) -> Union[Dict[str, Any], bool]:
        rule_context = {}
        for rule in self.rules:
            filter_result = await self._f_rule_event(rule=rule, event=event)
            if filter_result is False or filter_result is None:
                return False
            else:
                if not isinstance(filter_result, bool):
                    rule_context.update(filter_result)

        return rule_context

    async def handle(self, **context) -> Any:
        return await self.handler(**context)

    def __repr__(self):
        return f"<FromFuncHandler {self.handler.__name__} " f"rules={self.rules}>"
