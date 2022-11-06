import pytest

from .test_fsm import TestStates
from waio import Dispatcher, Bot
from waio.factory.factory import factory_gupshup
from waio.factory.models.main import BaseResponse
from waio.rules import StateRule
from waio.storage import RedisStorage
from waio.types import Event
from waio import F


bot = Bot(apikey="", src_name="", phone_number=12345678900)

storage = RedisStorage(
    prefix_fsm="fsm",
    redis_url="redis://default:pwd@192.168.1.102:6379"
)
dp = Dispatcher(bot=bot, storage=storage)


@pytest.mark.asyncio
async def test_check_state_filter_true():
    _state = dp.state(user_phone=79990000000)
    await _state.set_state(TestStates.email)
    message_json = {
        "app": "DemoApp",
        "timestamp": 1580227766370,
        "version": 2,
        "type": "message",
        "payload": {
            "id": "ABEGkYaYVSEEAhAL3SLAWwHKeKrt6s3FKB0c",
            "source": "79289998877",
            "type": "text",
            "payload": {"text": "Hi"},
            "sender": {
                "phone": "79990000000",
                "name": "Smit",
                "country_code": "7",
                "dial_code": "9990000000",
            },
        },
    }
    data_load = factory_gupshup.load(message_json, BaseResponse)
    message_model = Event(bot=dp.bot, message=data_load, state_func=dp.state)
    rule = StateRule(state=TestStates.email)

    check_filter = await rule.check(event=message_model)
    assert check_filter is True

    await _state.finish(clear_data=True)


@pytest.mark.asyncio
async def test_check_state_filter_false():
    _state = dp.state(user_phone=79990000000)
    await _state.set_state(TestStates.email)

    message_json = {
        "app": "DemoApp",
        "timestamp": 1580227766370,
        "version": 2,
        "type": "message",
        "payload": {
            "id": "ABEGkYaYVSEEAhAL3SLAWwHKeKrt6s3FKB0c",
            "source": "79289998877",
            "type": "text",
            "payload": {"text": "Hi"},
            "sender": {
                "phone": "79287776655",
                "name": "Anna",
                "country_code": "7",
                "dial_code": "9287776655",
            },
        },
    }
    data_load = factory_gupshup.load(message_json, BaseResponse)
    message_model = Event(bot=dp.bot, message=data_load, state_func=dp.state)
    rule = StateRule(state=TestStates.email)

    check_filter = await rule.check(event=message_model)
    assert check_filter is False

    await _state.finish(clear_data=True)


@pytest.mark.asyncio
async def test_magic_filter():
    _state = dp.state(user_phone=79990000000)
    await _state.set_state(TestStates.email)

    message_json = {
        "app": "DemoApp",
        "timestamp": 1580227766370,
        "version": 2,
        "type": "message",
        "payload": {
            "id": "ABEGkYaYVSEEAhAL3SLAWwHKeKrt6s3FKB0c",
            "source": "79289998877",
            "type": "text",
            "payload": {"text": "Hi"},
            "sender": {
                "phone": "79287776655",
                "name": "Anna",
                "country_code": "7",
                "dial_code": "9287776655",
            },
        },
    }
    data_load = factory_gupshup.load(message_json, BaseResponse)
    message_model = Event(bot=dp.bot, message=data_load, state_func=dp.state)
    rule = F.message.payload.sender.phone == 79287776655

    assert rule.resolve(message_model) is True

    await _state.finish(clear_data=True)
