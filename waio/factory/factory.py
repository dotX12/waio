from dataclass_factory import Factory, Schema
from waio.factory.models.basic import PayloadBaseModel
from waio.factory.models.button import PayloadButtonReply
from waio.factory.models.document import PayloadFile
from waio.factory.models.image import PayloadImage
from waio.factory.models.list import PayloadList
from waio.factory.models.text import PayloadText
from waio.factory.models.response import (
    ResponseMessagePayload,
    ResponseMessagePayloadPayload,
    ResponseUserEvent,
)
from waio.factory.models.contact import (
    PayloadContact,
    PayloadContactAddress,
    PayloadContactEmail,
    PayloadContactInformation,
    PayloadContactPhone,
    PayloadContactOrganization,
    PayloadContacts,
    PayloadContactUrl,
    PayloadSender,
)
from waio.factory.schemas import (
    BASE_MODEL,
    PAYLOAD_FILE,
    PAYLOAD_IMAGE,
    PAYLOAD_LIST,
    PAYLOAD_CONTACT,
    PAYLOAD_TEXT,
    PAYLOAD_SENDER,
    PAYLOAD_REPLY_KEYBOARD,
    CONTACTS_PAYLOAD,
    PAYLOAD_CONTACT_ADDRESS,
    PAYLOAD_CONTACT_ORGANIZATION,
    PAYLOAD_CONTACT_PHONE,
    PAYLOAD_CONTACT_URL,
    PAYLOAD_CONTACT_INFORMATION,
    RESPONSE_MESSAGE,
    PAYLOAD_CONTACT_EMAIL,
    RESPONSE_MESSAGE_PAYLOAD,
    RESPONSE_MESSAGE_PAYLOAD_PAYLOAD,
)

factory_gupshup = Factory(
    schemas={
        PayloadBaseModel: BASE_MODEL,
        PayloadText: PAYLOAD_TEXT,
        PayloadList: PAYLOAD_LIST,
        PayloadSender: PAYLOAD_SENDER,
        PayloadButtonReply: PAYLOAD_REPLY_KEYBOARD,
        PayloadImage: PAYLOAD_IMAGE,
        PayloadFile: PAYLOAD_FILE,
        PayloadContact: PAYLOAD_CONTACT,
        PayloadContacts: CONTACTS_PAYLOAD,
        PayloadContactOrganization: PAYLOAD_CONTACT_ORGANIZATION,
        PayloadContactPhone: PAYLOAD_CONTACT_PHONE,
        PayloadContactUrl: PAYLOAD_CONTACT_URL,
        PayloadContactInformation: PAYLOAD_CONTACT_INFORMATION,
        PayloadContactEmail: PAYLOAD_CONTACT_EMAIL,
        PayloadContactAddress: PAYLOAD_CONTACT_ADDRESS,
        ResponseUserEvent: RESPONSE_MESSAGE,
        ResponseMessagePayload: RESPONSE_MESSAGE_PAYLOAD,
        ResponseMessagePayloadPayload: RESPONSE_MESSAGE_PAYLOAD_PAYLOAD,
    },
    debug_path=True,
)

factory_default = Factory(default_schema=Schema(omit_default=True), debug_path=True)
