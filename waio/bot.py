from typing import Any, Dict, Optional

from waio.client.http import HTTPClient
from waio.factory.base import ResponseModel
from waio.factory.factory import factory_gupshup
from waio.gupshup.api import GupshupSettings
from waio.gupshup.form import generate_message_form
from waio.handlers.base_handlers import Handler, BaseHandlers
from waio.handlers.executor import HandlerExecutor
from waio.keyboard.list import ListMessage
from waio.labeler import BotLabeler
from waio.middleware import MiddlewareResponse
from waio.models.enums import GupshupMethods
from waio.models.text import MessageText
from waio.states.context import FSMContext
from waio.storage.redis import RedisStorage
from waio.types.message import Message
from waio.logs.logger import logger


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
        msg = MessageText(text=message)
        form = self.generate_form(receiver=receiver, message=msg)
        response = await self.request(
            headers=self._headers(),
            method='POST',
            url=GupshupMethods.message.value,
            data=form,
        )
        return response

    async def send_list(self, receiver: int, button: ListMessage):
        form = self.generate_form(receiver=receiver, message=button)

        response = await self.request(
            headers=self._headers(),
            method='POST',
            url=GupshupMethods.message.value,
            data=form,
        )
        return response


class Dispatcher(Handler, BaseHandlers):
    def __init__(self, bot: Bot, storage: Optional[RedisStorage] = None):
        self.bot = bot
        self.storage = storage
        self.labeler = BotLabeler()
        super().__init__(self.labeler)

    def state(self, user_phone: int) -> FSMContext:
        return FSMContext(storage=self.storage, user_phone=user_phone)

    async def handle_event(self, event: Dict[str, Any]) -> None:
        logger.debug(f'Event: - {event}')

        if event["type"] == "message":
            context_variables = {}

            data_load = factory_gupshup.load(event, ResponseModel)
            message = Message(bot=self.bot, message=data_load, state_func=self.state)

            for middleware in self.labeler.MIDDLEWARES:
                middleware.fill(event=message)
                response = await middleware.pre()

                logger.debug(f'[PRE]-Middleware: {middleware}')

                if response == MiddlewareResponse(False):
                    return
                elif isinstance(response, dict):
                    context_variables.update(response)

            logger.debug(f'[PRE]-Middleware values: {context_variables}')

            handle_responses = []
            current_handlers = []

            for handler in self.handlers:
                resp = await HandlerExecutor.execute(handler=handler, message=message, **context_variables)

                if resp:
                    handle_responses.append(resp)
                    current_handlers.append(handler)
                    await handler.handle(**resp)
                    break

            logger.debug(f'Handlers: {current_handlers}, Return: {handle_responses}')

            for middleware in self.labeler.MIDDLEWARES:
                middleware.fill(event=message, handlers=current_handlers, handle_responses=handle_responses)
                logger.debug(f'[POST]-Middleware - {middleware}')

                await middleware.post()


