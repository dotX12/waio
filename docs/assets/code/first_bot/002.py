loguru_filter.set_level("DEBUG")

bot = Bot(
    apikey="XXX",
    src_name="YYY",
    phone_number="PHONE",
)

dp = Dispatcher(bot=bot)
