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
        "callback":  CallbackFilter,
    }
    MIDDLEWARES: List[BaseMiddleware] = []

    def __init__(self):
        self._custom_rules = {}

    def bind_rule(self, name: str, value: ABCRule):
        self._custom_rules[name] = value

    @property
    def custom_rules(self):
        return self._custom_rules

    @property
    def default_rules(self):
        return self.DEFAULT_RULES

    def register_middleware(self, middleware):
        self.MIDDLEWARES.append(middleware)
