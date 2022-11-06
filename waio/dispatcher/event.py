from __future__ import annotations
from typing import TYPE_CHECKING, Union
from waio.handlers import FromFuncHandler
from waio.handlers import HandlerExecutor
from waio.middleware import MiddlewareResponse
from waio.models.system.handlers import ExecutedHandlerData

from waio.logs.logger import logger
from waio.types import Event
from waio.types.message import EventSubscribe

if TYPE_CHECKING:
    from waio.dispatcher.router import Router


class WhatsAppEventObserver:
    def __init__(self, router: Router, event_name: str):
        self.router = router
        self.event_name = event_name
        self._handlers = []

    def register(self, handler, *rules, **custom_rules):
        handler_object = FromFuncHandler(
            handler,
            *rules,
            *self.router.base_rules(**custom_rules),
            *self.router.custom_rules(**custom_rules),
        )
        self._handlers.append(handler_object)

    def __call__(self, *rules, **custom_rules):
        def wrapper(handler) -> None:
            self.register(handler=handler, *rules, **custom_rules)
            return handler

        return wrapper

    async def notify(self, event: Union[Event, EventSubscribe]):
        context_variables = {}
        for middleware in self.router.labeler.MIDDLEWARES:
            middleware.fill(event=event)
            response = await middleware.pre()

            logger.debug(f"[PRE]-Middleware: {middleware}")

            if response == MiddlewareResponse(False):
                logger.debug(f"[PRE]-Middleware: Exited...")
                return
            elif isinstance(response, dict):
                context_variables.update(response)

        logger.debug(f"[PRE]-Middleware values: {context_variables}")
        executed_handler_data = await self._resolve_handler(
            event=event, **context_variables
        )

        for middleware in reversed(self.router.labeler.MIDDLEWARES):
            middleware.fill(
                event=event,
                handler=executed_handler_data.handler,
                response=executed_handler_data.response,
            )
            await middleware.post()
            logger.debug(f"[POST]-Middleware - {middleware}")

    async def _resolve_handler(
        self, event: Event, **context_variables
    ) -> ExecutedHandlerData:
        for router in self.router.chain_tail:
            for handler in router.observers[self.event_name]._handlers:
                logger.debug(f"[Resolver]: Router: {router} Handler: {handler}")
                resp = await HandlerExecutor.execute(
                    handler=handler, event=event, **context_variables
                )
                if resp:
                    await handler.handle(**resp)
                    logger.debug(
                        f"[Result] Router: {router} Handler: {handler} Return {resp}"
                    )
                    return ExecutedHandlerData(
                        handler=handler,
                        response=resp,
                    )
        logger.debug(f"[Result] Router: None Handler: None Return None")
        return ExecutedHandlerData()
