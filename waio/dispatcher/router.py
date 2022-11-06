from __future__ import annotations

from typing import Dict
from typing import Generator
from typing import List
from typing import Optional
from typing import Union

from waio.dispatcher.event import WhatsAppEventObserver
from waio.handlers.base_handlers import HandlerRule
from waio.labeler import BotLabeler


class Router(HandlerRule):
    def __init__(
        self, *, name: Optional[str] = None, labeler: Optional[BotLabeler] = None
    ):
        self.labeler = labeler or BotLabeler()

        self.name = name or hex(id(self))
        self._parent_router: Optional[Router] = None
        self.sub_routers: List[Router] = []

        self.message_handler = WhatsAppEventObserver(router=self, event_name="message")
        self.notify_success_handler = WhatsAppEventObserver(
            router=self, event_name="opted-in"
        )
        self.notify_denied_handler = WhatsAppEventObserver(
            router=self, event_name="opted-out"
        )

        self.observers: Dict[str, WhatsAppEventObserver] = {
            "message": self.message_handler,
            "opted-in": self.notify_success_handler,
            "opted-out": self.notify_denied_handler,
        }
        super().__init__(self.labeler)

    def __str__(self) -> str:
        return f"{type(self).__name__} {self.name!r}"

    def __repr__(self) -> str:
        return f"<{self}>"

    @property
    def chain_head(self) -> Generator[Router, None, None]:
        router: Optional[Router] = self
        while router:
            yield router
            router = router.parent_router

    @property
    def chain_tail(self) -> Generator[Router, None, None]:
        yield self
        for router in self.sub_routers:
            yield from router.chain_tail

    @property
    def parent_router(self) -> Optional[Router]:
        return self._parent_router

    @parent_router.setter
    def parent_router(self, router: Router) -> None:
        """
        Internal property setter of parent router fot this router.
        Do not use this method in own code.
        All routers should be included via `include_router` method.

        Self- and circular- referencing are not allowed here

        :param router:
        """
        if not isinstance(router, Router):
            raise ValueError(
                f"router should be instance of Router not {type(router).__name__!r}"
            )
        if self._parent_router:
            raise RuntimeError(f"Router is already attached to {self._parent_router!r}")
        if self == router:
            raise RuntimeError("Self-referencing routers is not allowed")

        parent: Optional[Router] = router
        while parent is not None:
            if parent == self:
                raise RuntimeError("Circular referencing of Router is not allowed")

            parent = parent.parent_router

        self._parent_router = router
        router.sub_routers.append(self)

    def include_router(self, router: Union[Router, str]) -> Router:
        """
        Attach another router.

        Can be attached directly or by import string in format "<module>:<attribute>"

        :param router:
        :return:
        """
        if not isinstance(router, Router):
            raise ValueError(
                f"router should be instance of Router not {type(router).__class__.__name__}"
            )
        router.parent_router = self
        return router
