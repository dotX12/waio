from waio.middleware import BaseMiddleware
from waio.middleware import CancelHandler
from waio.middleware import ContinueHandler
from waio.middleware import MiddlewareResponse


class BanMiddleware(BaseMiddleware):
    def __init__(self):
        self.BAN_PHONES = [79283334455, 79283334477, 79185554433]

    async def pre(self):
        if self.event.message.payload.sender.phone in self.BAN_PHONES:
            await self.event.answer("Sorry, you are blocked.")
            return MiddlewareResponse(CancelHandler)
        return MiddlewareResponse(ContinueHandler)
