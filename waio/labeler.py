from typing import Dict, Type

from waio.rules.abc import ABCMessageRule
from waio.rules.default import (
    MessageCommandsRule,
    StateRule,
    RegexRule,
    ContentTypeRule,
    TextRuleEquals,
    TextRuleContains,
    TextRuleStartswith,
    TextRuleEndswith
)


class LabelerRules:
    DEFAULT_RULES: Dict[str, Type[ABCMessageRule]] = {
        "commands": MessageCommandsRule,
        "state": StateRule,
        "regexp": RegexRule,
        "text_equals": TextRuleEquals,
        "text_contains": TextRuleContains,
        "text_startswith": TextRuleStartswith,
        "text_endswith": TextRuleEndswith,
        "content_type": ContentTypeRule
    }

    def __init__(self):
        self._custom_rules = {}

    def bind_rule(self, name: str, value: ABCMessageRule):
        self._custom_rules[name] = value

    @property
    def custom_rules(self):
        return self._custom_rules

    @property
    def default_rules(self):
        return self.DEFAULT_RULES
