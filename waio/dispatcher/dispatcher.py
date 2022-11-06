from typing import Any
from typing import Dict
from typing import Optional

from waio import Bot
from waio.dispatcher.router import Router
from waio.dispatcher.event import WhatsAppEventObserver
from waio.factory.factory import factory_gupshup
from waio.factory.models.main import BaseResponse
from waio.factory.models.response import ResponseUserEvent
from waio.labeler import BotLabeler
from waio.logs.logger import logger
from waio.models.enums import EventPayloadType
from waio.models.enums import ResponseGupshupMessageType
from waio.states.context import FSMContext
from waio.storage.redis import RedisStorage
from waio.types.message import Event
from waio.types.message import EventSubscribe


class Dispatcher(Router):
    def __init__(
        self,
        bot: Bot,
        storage: Optional[RedisStorage] = None,
        name: Optional[str] = None
    ):
        self.bot = bot
        self.storage = storage
        self.labeler = BotLabeler()
        self.message_handler = WhatsAppEventObserver(router=self, event_name="message")
        self.notify_success_handler = WhatsAppEventObserver(router=self, event_name="opted-in")
        self.notify_denied_handler = WhatsAppEventObserver(router=self, event_name="opted-out")

        self.observers: Dict[str, WhatsAppEventObserver] = {
            "message": self.message_handler,
            "opted-in": self.notify_success_handler,
            "opted-out": self.notify_denied_handler,
        }
        super().__init__(name=name, labeler=self.labeler)

    def state(self, user_phone: int) -> FSMContext:
        return FSMContext(storage=self.storage, user_phone=user_phone)

    async def handle_event(self, event: Dict[str, Any]) -> None:
        try:
            # TODO: Refactoring
            logger.debug(f"Event: - {event}")
            if event.get("type", "") == "message":
                data_load = factory_gupshup.load(event, BaseResponse)
                event_obj = Event(
                    bot=self.bot,
                    message=data_load,
                    state_func=self.state
                )
                await self.observers["message"].notify(event=event_obj)

            if event.get("type", "") == ResponseGupshupMessageType.message_event:
                if event["payload"]["type"] == EventPayloadType.start_dialog:
                    data_load = factory_gupshup.load(event, ResponseUserEvent)
                    event_obj = EventSubscribe(
                        bot=self.bot,
                        message=data_load,
                        state_func=self.state
                    )
                    await self.observers["opted-in"].notify(event=event_obj)

        except Exception as exc:
            logger.exception("Exception", exc)
