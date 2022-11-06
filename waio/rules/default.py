import re
from typing import List, Union, Optional, Dict, Literal

from waio.rules.abc import ABCRule
from waio.states import BaseState
from waio.types.content_types import ContentType
from waio.types.message import Event
from waio.utils.callback.filters import CallbackDataFilterItem


class MessageCommandsRule(ABCRule):
    def __init__(self, commands: List[str], prefix: str = "/"):
        self.prefix = prefix
        self.commands = commands

    async def check(self, event: Event) -> bool:
        for command in self.commands:
            command_and_prefix = f"{self.prefix}{command}"
            if event.text.startswith(self.prefix):
                if command_and_prefix == event.text:
                    return True
        return False


class StateRule(ABCRule):
    def __init__(self, state: Optional[Union[BaseState, Literal["*"]]] = None):
        self.state = state

    async def check(self, event: Event) -> Union[dict, bool]:
        user_state = await event.current_state()
        if str(self.state) == user_state or not self.state or self.state == "*":
            return True
        return False


class RegexRule(ABCRule):
    def __init__(self, regexp: Union[str, List[str], re.Pattern, List[re.Pattern]]):
        if isinstance(regexp, re.Pattern):
            regexp = [regexp]
        elif isinstance(regexp, str):
            regexp = [re.compile(pattern=regexp)]
        elif isinstance(regexp, list):
            regexp = [re.compile(pattern=exp) for exp in regexp]

        self.regexp = regexp

    async def check(self, event: Event) -> Union[Dict[str, re.Match], bool]:
        for regexp in self.regexp:
            match = re.match(pattern=regexp, string=event.text)
            if match:
                return {"regex": match}
        return False


class TextRuleEquals(ABCRule):
    def __init__(self, equals: List[str]):
        self.equals = equals

    async def check(self, event: Event) -> bool:
        for elem in self.equals:
            if elem == event.text:
                return True
        return False


class TextRuleContains(ABCRule):
    def __init__(self, contains: List[str]):
        self.contains = contains

    async def check(self, event: Event) -> bool:
        for elem in self.contains:
            if elem in event.text:
                return True
        return False


class TextRuleStartswith(ABCRule):
    def __init__(self, startswith: List[str]):
        self.startswith = startswith

    async def check(self, event: Event) -> bool:
        for elem in self.startswith:
            if event.text.startswith(elem):
                return True
        return False


class TextRuleEndswith(ABCRule):
    def __init__(self, endswith: List[str]):
        self.endswith = endswith

    async def check(self, event: Event) -> bool:
        for elem in self.endswith:
            if event.text.endswith(elem):
                return True
        return False


class TextRule(ABCRule):
    def __init__(
        self,
        equals: Optional[List[str]] = None,
        contains: Optional[List[str]] = None,
        startswith: Optional[List[str]] = None,
        endswith: Optional[List[str]] = None,
    ):
        self.equals = equals
        self.contains = contains
        self.startswith = startswith
        self.endswith = endswith

    async def check(self, event: Event) -> bool:
        if self.equals:
            eq = TextRuleEquals(equals=self.equals)
            return await eq.check(event)

        if self.contains:
            ct = TextRuleContains(contains=self.equals)
            return await ct.check(event)

        if self.startswith:
            ss = TextRuleStartswith(startswith=self.startswith)
            return await ss.check(event)

        if self.endswith:
            es = TextRuleEndswith(endswith=self.endswith)
            return await es.check(event)


class ContentTypeRule(ABCRule):
    def __init__(self, content_types: List[ContentType]):
        self.content_types = content_types

    async def check(self, event: Event) -> Union[Dict[str, re.Match], bool]:
        for content_type in self.content_types:
            if isinstance(event.message.payload, content_type.value):
                return True
        return False


class PhoneNumberRule(ABCRule):
    def __init__(self, phones: List[int]):
        self.phones = phones

    async def check(self, event: Event) -> bool:
        for phone in self.phones:
            if phone == event.message.payload.sender.phone:
                return True
        return False


class CallbackFilter(ABCRule):
    def __init__(self, item: CallbackDataFilterItem):
        self.item = item

    async def check(self, event: Event) -> Union[bool, Dict[str, Dict[str, str]]]:
        return await self.item.check(event=event)
