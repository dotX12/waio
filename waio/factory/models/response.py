from dataclasses import dataclass
from uuid import uuid4

from waio.models.enums import ResponseGupshupMessageType, ResponseGupshupPayloadType, EventPayloadType


@dataclass
class ResponseMessagePayloadPayload:
    whatsapp_Message_id: str
    type: EventPayloadType


@dataclass
class ResponseMessagePayload:
    id: uuid4
    type: ResponseGupshupPayloadType
    destination: str
    payload: ResponseMessagePayloadPayload


@dataclass
class ResponseMessage:
    app: str
    timestamp: int
    version: int
    type: ResponseGupshupMessageType
    payload: ResponseMessagePayload


