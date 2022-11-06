from typing import Dict, Type, List

from waio.middleware import BaseMiddleware
from waio.rules.abc import ABCRule
from waio.rules.default import (
    MessageCommandsRule,
    StateRule,
    RegexRule,
    ContentTypeRule,
    TextRuleEquals,
    TextRuleContains,
    TextRuleStartswith,
    TextRuleEndswith,
    CallbackFilter,
)


class BotLabeler:
    DEFAULT_RULES: Dict[str, Type[ABCRule]] = {
        "commands": MessageCommandsRule,
        "state": StateRule,
        "regex": RegexRule,
        "text_equals": TextRuleEquals,
        "text_contains": TextRuleContains,
        "text_startswith": TextRuleStartswith,
        "text_endswith": TextRuleEndswith,
        "content_type": ContentTypeRule,
        "callback": CallbackFilter,
    }
    MIDDLEWARES: List[BaseMiddleware] = []
    CUSTOM_RULES: Dict[str, Type[ABCRule]] = {}

    def __str__(self):
        return f"BotLabeler custom_rules({self.CUSTOM_RULES}) middlewares ({self.MIDDLEWARES})"

    def bind_rule(self, name: str, value: Type[ABCRule]) -> None:
        self.CUSTOM_RULES[name] = value

    @property
    def custom_rules(self) -> Dict[str, Type[ABCRule]]:
        return self.CUSTOM_RULES

    @property
    def default_rules(self) -> Dict[str, Type[ABCRule]]:
        return self.DEFAULT_RULES

    def register_middleware(self, middleware: BaseMiddleware) -> None:
        self.MIDDLEWARES.append(middleware)
