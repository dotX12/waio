from typing import Optional, Dict, Any, Union


class BaseState:
    def __init__(
        self,
        state: Optional[str] = None,
        group: Optional[object] = None
    ):
        self._group = group
        self._state = state

    def __repr__(self):
        return f"<BaseState> {self.group.__name__}:{self.state}"

    def __str__(self):
        return f"{self.group.__name__}:{self.state}"

    def __set_name__(self, owner: "StatesGroup", name: str) -> None:
        self.group = owner
        self.state = name

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value


class StatesGroupMeta(type):
    __states__: Dict[str, Any]

    def __new__(mcs, cls_name, bases, attrs: Dict[str, Union[Any, BaseState]]):
        mcs.__states__ = {
            state_attr: state_value
            for state_attr, state_value in attrs.items()
            if not state_attr.startswith("__")
        }

        return super(StatesGroupMeta, mcs).__new__(
            mcs, cls_name, bases, attrs)


class StatesGroup(metaclass=StatesGroupMeta):
    pass
