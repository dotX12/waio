from waio.utils.callback.base_callback import CallbackDataBase
from waio.utils.callback.filters import CallbackDataFilterItem, CallbackDataFilterList


class CallbackItem(CallbackDataBase):

    def filter(self, **config) -> 'CallbackDataFilterItem':
        for key in config.keys():
            if key not in self._part_names:
                raise ValueError(f'Invalid field name {key!r}')
        return CallbackDataFilterItem(self, config)


class CallbackList(CallbackDataBase):

    def filter(self, **config) -> 'CallbackDataFilterList':
        for key in config.keys():
            if key not in self._part_names:
                raise ValueError(f'Invalid field name {key!r}')
        return CallbackDataFilterList(self, config)