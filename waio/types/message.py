from typing import Callable, Any

from waio.factory.base import ResponseModel
from waio.protocols.bot import Bot
from waio.states.context import FSMContext


class Message:
    def __init__(self, bot: Bot, message: ResponseModel, state_func: Callable[[int], FSMContext]):
        self.bot = bot
        self.message = message
        self._state_func = state_func

    @property
    def state(self):
        return self._state_func(self.message.payload.sender.phone)

    async def current_state(self) -> str:
        current_state = await self.state.get_state()
        return str(current_state)

    async def answer(self, message: str):
        await self.bot.send_message(receiver=self.message.payload.sender.phone, message=message)
