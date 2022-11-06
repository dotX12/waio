from enum import Enum

from waio.factory.models.button import PayloadButtonReply
from waio.factory.models.document import PayloadFile
from waio.factory.models.image import PayloadImage
from waio.factory.models.list import PayloadList
from waio.factory.models.text import PayloadText
from waio.factory.models.contact import PayloadContacts


class ContentType(Enum):
    TEXT = PayloadText
    FILE = PayloadFile
    PHOTO = PayloadImage
    CONTACT = PayloadContacts
    BUTTON = PayloadButtonReply
    LIST = PayloadList
