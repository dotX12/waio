import pytest
from waio import Bot, Dispatcher
from waio.states import StatesGroup, BaseState
from waio.logs import loguru_filter
from waio.storage import RedisStorage

loguru_filter.set_level("DEBUG")

bot = Bot(apikey="", src_name="", phone_number=12345678900)

storage = RedisStorage(
    prefix_fsm="fsm",
    redis_url="redis://default:pwd@192.168.1.102:6379"
)

dp = Dispatcher(bot=bot, storage=storage)


class TestStates(StatesGroup):
    birthday = BaseState()
    email = BaseState()


@pytest.mark.asyncio
async def test_clear_state():
    _state = dp.state(user_phone=79990000000)
    await _state.finish()
    current_state = await _state.get_state()
    assert current_state is None


@pytest.mark.asyncio
async def test_set_state():
    _state = dp.state(user_phone=79990000000)
    await _state.finish()
    await _state.set_state(TestStates.email)
    current_state = await _state.get_state()
    assert current_state == str(TestStates.email)

    await _state.finish(clear_data=True)


@pytest.mark.asyncio
async def test_check_set_state():
    _state = dp.state(user_phone=79990000000)
    await _state.set_state(TestStates.email)
    current_state = await _state.get_state()
    assert current_state == str(TestStates.email)
    await _state.finish()


@pytest.mark.asyncio
async def test_check_get_set_data():
    _state = dp.state(user_phone=79990000000)
    await _state.set_data(foo="bar", baz="baq")
    current_data = await _state.get_data()
    assert current_data == {"baz": "baq", "foo": "bar"}
    await _state.finish(clear_data=True)


@pytest.mark.asyncio
async def test_check_get_set_data_keys():
    _state = dp.state(user_phone=79990000000)
    await _state.set_data(foo="foo_value", bar="bar_value")

    current_data = await _state.get_data("foo")
    assert current_data == {"foo": "foo_value"}

    current_data = await _state.get_data("foo", "bar")
    assert current_data == {"foo": "foo_value", "bar": "bar_value"}

    await _state.finish(clear_data=True)


@pytest.mark.asyncio
async def test_check_get_set_data_keys():
    _state = dp.state(user_phone=79990000000)
    await _state.set_data(foo="foo_value", bar="bar_value")

    current_data = await _state.get_data("foo")
    assert current_data == {"foo": "foo_value"}

    current_data = await _state.get_data("foo", "bar")
    assert current_data == {"foo": "foo_value", "bar": "bar_value"}

    await _state.finish(clear_data=True)
