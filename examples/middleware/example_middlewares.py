from waio.logs import logger
from waio.middleware import (
    BaseMiddleware,
    MiddlewareResponse,
    CancelHandler,
    ContinueHandler,
)
from examples.middleware.database import ExampleDatabase


class BanMiddleware(BaseMiddleware):
    def __init__(self):
        self.BAN_PHONES = [79283334455, 79283334477, 79185554433]

    async def pre(self):
        if self.event.message.payload.sender.phone in self.BAN_PHONES:
            await self.event.answer("Sorry, you are blocked.")
            return MiddlewareResponse(CancelHandler)
        return MiddlewareResponse(ContinueHandler)


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self):
        self.session = ExampleDatabase()

    async def pre(self):
        self.session.open_session()
        self.session.set("key_pre", "value")

        logger.info(
            f"[PRE]-DatabaseMiddleware conn: {self.session.session} values: {self.session.data}"
        )
        return {"session": self.session}

    async def post(self):
        self.session.set("key_post", "value")
        self.session.close_session()

        logger.info(
            f"[POST]-DatabaseMiddleware conn: {self.session.session} values: {self.session.data}"
        )
