import logging
from typing import Any, Dict
import inspect
from pydantic import BaseModel, Field

from waio.client.http import HTTPClient
from waio.factory.base import ResponseModel
from waio.factory.factory import factory_gupshup
from waio.gupshup.api import GupshupSettings
from waio.gupshup.form import generate_message_form
from waio.handlers.base_handlers import Handler, BaseHandlers
from waio.handlers.executor import HandlerExecutor
from waio.labeler import LabelerRules
from waio.models.enums import GupshupMethods
from waio.states.context import FSMContext
from waio.storage.redis import RedisStorage
from waio.types.message import Message

logger = logging.getLogger(__name__)
logging.basicConfig()
logger.setLevel(logging.DEBUG)


class MessageText(BaseModel):
    text: str = Field(...)


class MessageTextType(MessageText):
    type: str = Field(default='text')


class Bot(GupshupSettings, HTTPClient):

    def __init__(self, apikey: str, src_name: str, phone_number: int):
        super().__init__(apikey=apikey, src_name=src_name, phone_number=phone_number)

    def generate_form(self, receiver, message):
        return generate_message_form(
            source=self.phone_number,
            receiver=receiver,
            app_name=self.src_name,
            message=message.json()
        )

    async def send_message(self, receiver: int, message: str):
        # TODO: НАДО УБРАТЬ, ТЕСТИРУЮ ДЛЯ БОТА.
        msg = MessageTextType(text=message)
        form = self.generate_form(receiver=receiver, message=msg)
        response = await self.request(
            headers=self._headers(),
            method='POST',
            url=GupshupMethods.message.value,
            data=form,
        )
        return response


class Dispatcher(Handler, BaseHandlers):
    def __init__(self, bot: Bot, storage: RedisStorage):
        self.bot = bot
        self.storage = storage
        self.labeler = LabelerRules()
        super().__init__(self.labeler)

    def state(self, user_phone: int) -> FSMContext:
        return FSMContext(storage=self.storage, user_phone=user_phone)

    async def handle_event(self, event: Dict[str, Any]) -> None:
        data_load = factory_gupshup.load(event, ResponseModel)
        message_object = Message(bot=self.bot, message=data_load, state_func=self.state)

        for handler in self.handlers:
            await HandlerExecutor.execute(handler=handler, message=message_object)



