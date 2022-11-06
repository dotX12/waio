from waio import Router
from .handlers_1 import router1
from .handlers_2 import router2

own_router = Router(name="Own Router")
own_router.include_router(router1)
own_router.include_router(router2)
