from __future__ import annotations
import inspect
from typing import Optional, Dict, Any, TYPE_CHECKING
from waio.types.message import Event

if TYPE_CHECKING:
    from waio.handlers import FromFuncHandler


class HandlerExecutor:
    @classmethod
    async def execute(
        cls, handler: FromFuncHandler, event: Event, **middleware_kwargs
    ) -> Optional[Dict[str, Any]]:
        handler_filter = await handler.filter(event=event)
        if isinstance(handler_filter, dict):
            values_handler = {
                "event": event,
                "state": event.state,
                **handler_filter,
                **middleware_kwargs,
            }
            func_info = inspect.getfullargspec(handler.handler)
            values_to_func = {
                key: value
                for key, value in values_handler.items()
                if key in func_info.args
            }
            return values_to_func
        return None
