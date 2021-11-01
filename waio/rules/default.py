import re
from typing import List, Any, Union, Optional, Dict

from waio.rules.abc import ABCMessageRule
from waio.types.content_types import ContentType
from waio.types.message import Message


class MessageCommandsRule(ABCMessageRule):
    def __init__(self, commands: List[str], prefix: str = "/"):
        self.prefix = prefix
        self.commands = commands

    async def check(self, message: Message) -> bool:
        text = message.message.payload.text

        for command in self.commands:
            command_and_prefix = f"{self.prefix}{command}"

            if text.startswith(self.prefix):
                if command_and_prefix == text:
                    return True
        return False


class StateRule(ABCMessageRule):
    def __init__(self, state: Any):
        self.state = state

    async def check(self, message: Message) -> Union[dict, bool]:
        user_state = await message.current_state()
        if str(self.state) == user_state:
            return True
        return False


class RegexRule(ABCMessageRule):
    def __init__(self, regexp: Union[str, List[str], re.Pattern, List[re.Pattern]]):
        if isinstance(regexp, re.Pattern):
            regexp = [regexp]
        elif isinstance(regexp, str):
            regexp = [re.compile(regexp)]
        elif isinstance(regexp, list):
            regexp = [re.compile(exp) for exp in regexp]

        self.regexp = regexp

    async def check(self, message: Message) -> Union[Dict[str, re.Match], bool]:
        for regexp in self.regexp:
            match = re.match(regexp, message.message.payload.text)
            if match:
                return {"regexp": match}
        return False


class TextRuleEquals(ABCMessageRule):
    def __init__(self, equals: str):
        self.equals = equals

    async def check(self, message: Message) -> bool:
        return self.equals == message.message.payload.text


class TextRuleContains(ABCMessageRule):
    def __init__(self, contains: str):
        self.contains = contains

    async def check(self, message: Message) -> bool:
        return self.contains in message.message.payload.text


class TextRuleStartswith(ABCMessageRule):
    def __init__(self, startswith: str):
        self.startswith = startswith

    async def check(self, message: Message) -> bool:
        return message.message.payload.text.startswith(self.startswith)


class TextRuleEndswith(ABCMessageRule):
    def __init__(self, endswith: str):
        self.endswith = endswith

    async def check(self, message: Message) -> bool:
        return message.message.payload.text.endswith(self.endswith)


class TextRule(ABCMessageRule):
    def __init__(
        self,
        equals: Optional[str] = None,
        contains: Optional[str] = None,
        startswith: Optional[str] = None,
        endswith: Optional[str] = None
    ):
        self.equals = equals
        self.contains = contains
        self.startswith = startswith
        self.endswith = endswith

    async def check(self, message: Message) -> bool:
        if self.equals:
            eq = TextRuleEquals(equals=self.equals)
            return await eq.check(message)

        if self.contains:
            ct = TextRuleContains(contains=self.equals)
            return await ct.check(message)

        if self.startswith:
            ss = TextRuleStartswith(startswith=self.startswith)
            return await ss.check(message)

        if self.endswith:
            es = TextRuleEndswith(endswith=self.endswith)
            return await es.check(message)


class ContentTypeRule(ABCMessageRule):
    def __init__(self, content_types: List[ContentType]):
        self.content_types = content_types

    async def check(self, message: Message) -> Union[Dict[str, re.Match], bool]:
        for content_type in self.content_types:
            if isinstance(message.message.payload, content_type.value):
                return True
        return False


class PhoneNumberRule(ABCMessageRule):
    def __init__(self, phones: List[int]):
        self.phones = phones

    async def check(self, message: Message) -> bool:
        for phone in self.phones:
            if phone == message.message.payload.sender.phone:
                return True
        return False
