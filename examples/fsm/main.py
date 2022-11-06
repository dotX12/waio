from aiohttp import web
from waio import Bot, Dispatcher
from waio.states import StatesGroup, BaseState, FSMContext
from waio.types import Event
from waio.logs import loguru_filter
from waio.storage import RedisStorage

loguru_filter.set_level("DEBUG")

bot = Bot(apikey="API_KEY", src_name="SRC_NAME", phone_number=79281112233)

storage = RedisStorage(prefix_fsm="fsm", redis_url="redis://localhost:6379")
dp = Dispatcher(bot=bot, storage=storage)


class RegisterStates(StatesGroup):
    birthday = BaseState()
    email = BaseState()


@dp.message_handler(commands=["register"], state="*")
async def register_name(event: Event, state: FSMContext):
    await event.answer(f"Hi, {event.sender_name}! send your date of birth")
    await state.set_state(RegisterStates.birthday)


@dp.message_handler(state=RegisterStates.birthday)
async def register_age(event: Event, state: FSMContext):
    await state.set_data(birthday=event.text)
    await event.answer(f"Thanks for sending you birthday!\n" f"Send you email address")
    await state.set_state(RegisterStates.email)


@dp.message_handler(state=RegisterStates.email)
async def register_age(event: Event, state: FSMContext):
    await state.set_data(email=event.text)
    state_data_certain = await state.get_data("email", "birthday")
    # Alternative for get all data:
    # await state.get_data()

    await event.answer(
        f"Register completed...\n\n"
        f"Your name: {event.sender_name}\n"
        f'Your email: {state_data_certain["email"]}\n'
        f'Your birthday: {state_data_certain["birthday"]}\n'
    )

    await state.finish(clear_data=True)


async def handler_gupshup(request):
    event = await request.json()
    await dp.handle_event(event)
    return web.Response(status=200)


if __name__ == "__main__":
    webhook = web.Application()
    webhook.add_routes([web.post("/api/v1/gupshup/hook", handler_gupshup)])
    web.run_app(webhook, port=8017)
