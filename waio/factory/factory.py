from dataclass_factory import Factory, Schema
from waio.factory.models.basic import PayloadBaseModel
from waio.factory.models.button import PayloadButtonReply
from waio.factory.models.document import PayloadFile
from waio.factory.models.image import PayloadImage
from waio.factory.models.list import PayloadList
from waio.factory.models.text import PayloadText
from waio.factory.schemas import Schemas
from waio.factory.models.response import ResponseMessagePayload, ResponseMessagePayloadPayload, ResponseMessage
from waio.factory.models.contact import (
    PayloadContact,
    PayloadContactAddress,
    PayloadContactEmail,
    PayloadContactInformation,
    PayloadContactPhone,
    PayloadContactOrganization,
    PayloadContacts,
    PayloadContactUrl,
    PayloadSender
)


factory_gupshup = Factory(
    schemas={
        PayloadBaseModel: Schemas.BASE_MODEL,
        PayloadText: Schemas.PAYLOAD_TEXT,
        PayloadList: Schemas.PAYLOAD_LIST,
        PayloadSender: Schemas.PAYLOAD_SENDER,
        PayloadButtonReply: Schemas.PAYLOAD_REPLY_KEYBOARD,
        PayloadImage: Schemas.PAYLOAD_IMAGE,
        PayloadFile: Schemas.PAYLOAD_FILE,
        PayloadContact: Schemas.PAYLOAD_CONTACT,
        PayloadContacts: Schemas.CONTACTS_PAYLOAD,
        PayloadContactOrganization: Schemas.PAYLOAD_CONTACT_ORGANIZATION,
        PayloadContactPhone: Schemas.PAYLOAD_CONTACT_PHONE,
        PayloadContactUrl: Schemas.PAYLOAD_CONTACT_URL,
        PayloadContactInformation: Schemas.PAYLOAD_CONTACT_INFORMATION,
        PayloadContactEmail: Schemas.PAYLOAD_CONTACT_EMAIL,
        PayloadContactAddress: Schemas.PAYLOAD_CONTACT_ADDRESS,
        ResponseMessage: Schemas.RESPONSE_MESSAGE,
        ResponseMessagePayload: Schemas.RESPONSE_MESSAGE_PAYLOAD,
        ResponseMessagePayloadPayload: Schemas.RESPONSE_MESSAGE_PAYLOAD_PAYLOAD
}, debug_path=True)

factory_default = Factory(
    default_schema=Schema(omit_default=True),
    debug_path=True
)
