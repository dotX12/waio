from typing import List
from waio.labeler import BotLabeler
from waio.rules import ABCRule


class HandlerRule:
    def __init__(self, labeler: BotLabeler):
        self.labeler = labeler

    def base_rules(self, **rules) -> List[ABCRule]:
        return [
            self.labeler.default_rules[k](v)  # type: ignore
            for k, v in rules.items()
            if k in self.labeler.default_rules.keys()
        ]

    def custom_rules(self, **rules) -> List[ABCRule]:
        return [
            self.labeler.custom_rules[k](v)  # type: ignore
            for k, v in rules.items()
            if k in self.labeler.custom_rules.keys()
        ]
