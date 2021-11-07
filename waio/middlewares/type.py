from typing import NewType

MiddlewareResponse = NewType("MiddlewareResponse", bool)
CancelHandler = False
ContinueHandler = True
