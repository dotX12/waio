from dataclasses import dataclass
from typing import Union

from waio.factory.models.button import PayloadButtonReply
from waio.factory.models.contact import PayloadContacts
from waio.factory.models.document import PayloadFile
from waio.factory.models.image import PayloadImage
from waio.factory.models.list import PayloadList
from waio.factory.models.text import PayloadText


@dataclass
class BaseResponse:
    app: str
    type: str
    payload: Union[
        PayloadList,
        PayloadText,
        PayloadButtonReply,
        PayloadImage,
        PayloadFile,
        PayloadContacts
    ]
