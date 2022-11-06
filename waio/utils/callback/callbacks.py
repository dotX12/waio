from waio.utils.callback.base_callback import CallbackDataBase
from waio.utils.callback.filters import CallbackDataFilterItem, CallbackDataFilterGroup


class CallbackDataItem(CallbackDataBase):
    def filter(self, **config) -> "CallbackDataFilterItem":
        for key in config.keys():
            if key not in self._part_names:
                raise ValueError(f"Invalid field name {key!r}")
        return CallbackDataFilterItem(self, config)


class CallbackDataGroup(CallbackDataBase):
    def filter(self, **config) -> "CallbackDataFilterGroup":
        for key in config.keys():
            if key not in self._part_names:
                raise ValueError(f"Invalid field name {key!r}")
        return CallbackDataFilterGroup(self, config)
