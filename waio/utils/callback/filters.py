from waio.types import Message
from waio.utils.callback.base_filter import CallbackDataFilterBase


class CallbackDataFilterGroup(CallbackDataFilterBase):
    async def check(self, message: Message):
        return await self.base_check(message.callback_data_list)


class CallbackDataFilterItem(CallbackDataFilterBase):
    async def check(self, message: Message):
        return await self.base_check(message.callback_data_item)
