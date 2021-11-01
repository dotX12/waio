from enum import Enum


class RequestMethods(str, Enum):
    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


class ResponseGupshupMessageType(str, Enum):
    request = 'message'
    message_event = 'message-event'
    event = 'user-event'


class ResponseGupshupPayloadType(str, Enum):
    enqueued = 'enqueued'
    text = 'text'
    file = 'file'
    contact = 'contact'
    image = 'image'


class EventPayloadType(str, Enum):
    start_dialog = 'opted-in'
    session = 'session'
    sandbox_start = 'SANDBOX_START'
    failed = 'failed'


class GupshupMethods(str, Enum):
    message = 'https://api.gupshup.io/sm/api/v1/msg'

