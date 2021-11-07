from typing import List, Callable

from waio.handlers.func_handler import FromFuncHandler
from waio.labeler import BotLabeler


class BaseHandlers:

    def __init__(self, labeler: BotLabeler):
        self.handlers: List[FromFuncHandler] = []
        self.labeler = labeler

    def add_message_handler(self, handler):
        self.handlers.append(handler)

    def register_message_handler(
        self,
        handler: Callable,
        *rules,
        **custom_rules,
    ):
        handler_object = FromFuncHandler(
            handler,
            *rules,
            *self.base_rules(**custom_rules),
            *self.custom_rules(**custom_rules)
        )
        self.add_message_handler(handler=handler_object)

    def base_rules(self, **rules):
        default_rules = [
            self.labeler.default_rules[k](v)
            for k, v in rules.items()
            if k in self.labeler.default_rules.keys()
        ]

        return default_rules

    def custom_rules(self, **rules):
        custom = [
            self.labeler.custom_rules[k](v)
            for k, v in rules.items()
            if k in self.labeler.custom_rules.keys()
        ]

        return custom


class Handler(BaseHandlers):

    def message_handler(
        self,
        *rules,
        **custom_rules
    ):
        def decorator(handler) -> None:

            handler_object = FromFuncHandler(
                handler,
                *rules,
                *self.base_rules(**custom_rules),
                *self.custom_rules(**custom_rules)
            )
            self.add_message_handler(handler=handler_object)

            return handler
        return decorator
