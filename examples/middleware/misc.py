from waio import Bot, Dispatcher
from waio.logs import loguru_filter

from examples.middleware.example_middlewares import BanMiddleware, DatabaseMiddleware

loguru_filter.set_level("DEBUG")

bot = Bot(apikey="API_KEY", src_name="SRC_NAME", phone_number=7928994433)

dp = Dispatcher(bot=bot)

dp.labeler.register_middleware(BanMiddleware())
dp.labeler.register_middleware(DatabaseMiddleware())
