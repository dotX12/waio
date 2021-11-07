import inspect
from typing import Optional, Dict, Any

from waio.handlers.func_handler import FromFuncHandler
from waio.types.message import Message
from waio.logs.logger import logger


class HandlerExecutor:

    @classmethod
    async def execute(cls, handler: FromFuncHandler, message: Message, **middleware_kwargs) -> Optional[Dict[str, Any]]:
        handler_filter = await handler.filter(message)

        if isinstance(handler_filter, dict):
            values_handler = {"message": message, "state": message.state, **handler_filter, **middleware_kwargs}
            func_info = inspect.getfullargspec(handler.handler)
            values_to_func = {key: value for key, value in values_handler.items() if key in func_info.args}
            return values_to_func
        return None
