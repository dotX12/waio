from typing import Callable, Any

from waio.factory.base import ResponseModel
from waio.protocols.bot import Bot
from waio.states.context import FSMContext


class MessagePropertyEvent:
    def __init__(self, message: ResponseModel):
        self.message = message

    @property
    def text(self) -> str:
        if hasattr(self.message.payload, 'caption') and self.message.payload.caption:
            return self.message.payload.caption
        if hasattr(self.message.payload, 'text') and self.message.payload.text:
            return self.message.payload.text
        return ''

    @property
    def sender_number(self):
        return self.message.payload.sender.phone

    @property
    def sender_name(self):
        return self.message.payload.sender.name


class Message(MessagePropertyEvent):
    def __init__(self, bot: Bot, message: ResponseModel, state_func: Callable[[int], FSMContext]):
        self.bot = bot
        self.message = message
        self._state_func = state_func

        super().__init__(message)

    @property
    def state(self):
        return self._state_func(self.message.payload.sender.phone)

    async def current_state(self) -> str:
        current_state = await self.state.get_state()
        return str(current_state)

    async def answer(self, message: str):
        await self.bot.send_message(receiver=self.message.payload.sender.phone, message=message)
