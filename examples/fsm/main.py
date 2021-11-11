from aiohttp import web
from waio import Bot, Dispatcher
from waio.states import StateGroup, BaseState, FSMContext
from waio.types import Message
from waio.logs import loguru_filter
from waio.storage import RedisStorage

loguru_filter.set_level('DEBUG')

bot = Bot(
    apikey='API_KEY',
    src_name='SRC_NAME',
    phone_number=79281112233
)

storage = RedisStorage(prefix_fsm='fsm', redis_url="redis://localhost:6379")
dp = Dispatcher(bot=bot, storage=storage)


class RegisterState(StateGroup):
    birthday = BaseState()
    email = BaseState()


@dp.message_handler(commands=['register'], state='*')
async def register_name(message: Message, state: FSMContext):
    await message.answer(f'Hi, {message.sender_name}! send your date of birth')
    await state.set_state(RegisterState.birthday)


@dp.message_handler(state=RegisterState.birthday)
async def register_age(message: Message, state: FSMContext):
    await state.set_data(birthday=message.text)
    await message.answer(f'Thanks for sending you birthday!\n'
                         f'Send you email address')
    await state.set_state(RegisterState.email)


@dp.message_handler(state=RegisterState.email)
async def register_age(message: Message, state: FSMContext):
    await state.set_data(email=message.text)
    state_data_certain = await state.get_data("email", "birthday")
    # Alternative for get all data:
    # await state.get_data()

    await message.answer(f'Register completed...\n\n'
                         f'Your name: {message.sender_name}\n'
                         f'Your email: {state_data_certain["email"]}\n'
                         f'Your birthday: {state_data_certain["birthday"]}\n')

    await state.finish(clear_data=True)


async def handler_gupshup(request):
    event = await request.json()
    await dp.handle_event(event)
    return web.Response(status=200)


if __name__ == "__main__":
    webhook = web.Application()
    webhook.add_routes([web.post('/api/v1/gupshup/hook', handler_gupshup)])
    web.run_app(webhook, port=8017)
