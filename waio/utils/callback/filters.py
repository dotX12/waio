from waio.types import Event
from waio.utils.callback.base_filter import CallbackDataFilterBase


class CallbackDataFilterGroup(CallbackDataFilterBase):
    async def check(self, event: Event):
        return await self.base_check(event.callback_data_list)


class CallbackDataFilterItem(CallbackDataFilterBase):
    async def check(self, event: Event):
        return await self.base_check(event.callback_data_item)
