from abc import ABC
from typing import List, Any


class BaseMiddleware(ABC):
    async def pre(self, event):
        ...

    async def post(
        self, event, handle_responses: List[Any], handler: Any
    ):
        ...

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"
