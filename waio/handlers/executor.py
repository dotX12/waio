import inspect
from typing import Optional, Dict, Any

from waio.handlers import ABCHandler
from waio.types.message import Message


class HandlerExecutor:

    @classmethod
    async def execute(cls, handler: ABCHandler, message: Message, **middleware_kwargs) -> Optional[Dict[str, Any]]:
        handler_filter = await handler.filter(message)

        if isinstance(handler_filter, dict):
            values_handler = {"message": message, "state": message.state, **handler_filter, **middleware_kwargs}
            func_info = inspect.getfullargspec(handler.handler)
            values_to_func = {key: value for key, value in values_handler.items() if key in func_info.args}
            return values_to_func
        return None
