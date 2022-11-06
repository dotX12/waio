from typing import Callable
from typing import Optional

from waio.factory.models.main import BaseResponse
from waio.factory.models.response import ResponseUserEvent
from waio.protocols.bot import Bot
from waio.states.context import FSMContext


class MessagePropertyEvent:
    def __init__(self, message: BaseResponse):
        self.message = message

    @property
    def text(self) -> str:
        if hasattr(self.message.payload, "caption") and self.message.payload.caption:
            return self.message.payload.caption
        if hasattr(self.message.payload, "text") and self.message.payload.text:
            return self.message.payload.text
        return ""

    @property
    def sender_number(self) -> int:
        return self.message.payload.sender.phone

    @property
    def sender_name(self) -> str:
        return self.message.payload.sender.name

    @property
    def callback_data_item(self) -> Optional[str]:
        if (
            hasattr(self.message.payload, "postback_text")
            and self.message.payload.postback_text
        ):
            return self.message.payload.postback_text
        return ""

    @property
    def callback_data_list(self) -> Optional[str]:
        if hasattr(self.message.payload, "id") and self.message.payload.id:
            return self.message.payload.id
        return ""


class Event(MessagePropertyEvent):
    def __init__(
        self, bot: Bot, message: BaseResponse, state_func: Callable[[int], FSMContext]
    ):
        self.bot = bot
        self.message = message
        self._state_func = state_func

        super().__init__(message)

    @property
    def state(self) -> FSMContext:
        return self._state_func(self.message.payload.sender.phone)

    async def current_state(self) -> str:
        current_state = await self.state.get_state()
        return str(current_state)

    async def answer(self, message: str):
        await self.bot.send_message(
            receiver=self.message.payload.sender.phone, message=message
        )


class EventSubscribe:
    def __init__(
        self,
        bot: Bot,
        message: ResponseUserEvent,
        state_func: Callable[[int], FSMContext],
    ):
        self.bot = bot
        self.message = message
        self._state_func = state_func

    @property
    def state(self) -> FSMContext:
        return self._state_func(self.message.payload.phone)

    async def current_state(self) -> str:
        current_state = await self.state.get_state()
        return str(current_state)

    async def answer(self, message: str):
        await self.bot.send_message(
            receiver=self.message.payload.phone, message=message
        )
