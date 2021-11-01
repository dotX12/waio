import inspect
from typing import Union, Callable, Optional, Dict, Any, Awaitable

from waio.factory.base import ResponseModel
from waio.factory.factory import factory_gupshup
from waio.handlers.func_handler import FromFuncHandler
from waio.protocols.bot import Bot
from waio.states.context import FSMContext
from waio.types.message import Message


class HandlerExecutor:

    @classmethod
    async def execute(cls, handler: FromFuncHandler, message: Message) -> Optional[Callable[[Dict[str, Any]], Awaitable]]:

        if message.message.type == 'message':
            handler_filter = await handler.filter(message)

            if isinstance(handler_filter, dict):
                values_handler = {"message": message, "state": message.state, **handler_filter}
                func_info = inspect.getfullargspec(handler.handler)
                values_to_func = {key: value for key, value in values_handler.items() if key in func_info.args}

                return await handler.handle(**values_to_func)
        return None
