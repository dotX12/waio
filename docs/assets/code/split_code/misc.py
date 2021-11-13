from aiohttp import web

from waio.bot import Bot, Dispatcher
from waio.logs import loguru_filter
from waio.storage import RedisStorage

loguru_filter.set_level('DEBUG')

storage = RedisStorage(prefix_fsm='fsm', redis_url="redis://localhost:6379")

bot = Bot(
    apikey='API_KEY',
    src_name='SRC_NAME',
    phone_number=7928994433
)

dp = Dispatcher(bot=bot, storage=storage)

webhook = web.Application()
