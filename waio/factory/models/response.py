from dataclasses import dataclass
from dataclasses import field
from typing import Optional
from uuid import uuid4

from waio.models.enums import (
    ResponseGupshupMessageType,
    ResponseGupshupPayloadType,
    EventPayloadType,
)


@dataclass
class ResponseMessagePayloadPayload:
    type: EventPayloadType
    whatsapp_Message_id: Optional[str] = field(default=None)
    phone: Optional[int] = field(default=None)


@dataclass
class ResponseMessagePayload:
    # id: uuid4
    type: EventPayloadType
    phone: int
    # destination: str
    # payload: ResponseMessagePayloadPayload


@dataclass
class ResponseUserEvent:
    app: str
    timestamp: int
    version: int
    type: ResponseGupshupMessageType
    payload: ResponseMessagePayload
