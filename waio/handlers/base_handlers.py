import logging
from typing import Optional, List

from waio.handlers.message import HandlerStorage
from waio.states.fsm import BaseState

logger = logging.getLogger(__name__)
logging.basicConfig()
logger.setLevel(logging.DEBUG)


class BaseHandlers(HandlerStorage):

    def __init__(self):
        self.handlers: List = []
        self.middlewares: List = []

    def add_message_handler(self, handler):
        self.handlers.append(handler)

    @staticmethod
    def _build_handler_dict(handler, *args, **filters):
        logger.debug(f'DEBUG _build_handler_dict - {args=}, {filters=}')

        return {
            'function': handler,
            'filters': {f_type: f_value for f_type, f_value in filters.items() if f_value is not None}
        }

    def register_message_handler(
        self,
        func,
        commands: Optional[List[str]] = None,
        state: Optional[BaseState] = None,
        regexp: Optional[str] = None,
    ):
        handler = self._build_handler_dict(
            handler=func,
            commands=commands,
            state=state,
            regexp=regexp,
        )
        self.add_message_handler(handler=handler)

    @staticmethod
    async def call_handler(handler, *args, **kwargs):
        return await handler(*args, **kwargs)


class Handler(BaseHandlers):

    def message_handler(
        self,
        commands: List[str] = None,
        func=None,
        content_types=None,
        chat_types=None,
        state=None,
        regexp=None,
    ):
        def decorator(handler) -> None:
            handler_dict = self._build_handler_dict(
                handler=handler,
                chat_types=chat_types,
                content_types=content_types,
                commands=commands,
                func=func,
                state=state,
                regexp=regexp
            )
            self.add_message_handler(handler=handler_dict)
            return handler

        return decorator
