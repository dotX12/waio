from typing import Union

from waio.factory.models.main import BaseResponse
from waio.factory.models.response import ResponseMessage

ResponseModel = Union[ResponseMessage, BaseResponse]
