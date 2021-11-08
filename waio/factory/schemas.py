from dataclass_factory import Schema
from dataclass_factory.schema_helpers import type_checker


class Schemas:
    PAYLOAD_TEXT = Schema(
        name_mapping={
            "payload_id": "id",
            "type": "type",
            "text": ("payload", "text"),
        },
        skip_internal=True
    )

    PAYLOAD_SENDER = Schema(
        name_mapping={
            "phone": "phone",
            "name": "name",
        },
        skip_internal=True
    )

    PAYLOAD_LIST = Schema(
        name_mapping={
            "payload_id": "id",
            "type": "type",
            "title": ("payload", "title"),
            "id": ("payload", "id"),
            "reply": ("payload", "reply"),
            "postback_text": ("payload", "postbackText"),
            "description": ("payload", "description"),
        },
        pre_parse=type_checker("list_reply", field="type"),
        skip_internal=True
    )

    PAYLOAD_REPLY_KEYBOARD = Schema(
        name_mapping={
            "payload_id": "id",
            "type": "type",
            "title": ("payload", "title"),
            "id": ("payload", "id"),
            "reply": ("payload", "reply"),
        },
        pre_parse=type_checker(value="button_reply", field="type"),
        skip_internal=True
    )

    PAYLOAD_IMAGE = Schema(
        name_mapping={
            "payload_id": "id",
            "type": "type",
            "url": ("payload", "url"),
            "content_type": ("payload", "contentType"),
            "url_expiry": ("payload", "urlExpiry"),
            "caption": ("payload", "caption")
        },
        pre_parse=type_checker(value="image", field="type"),
        skip_internal=True
    )

    PAYLOAD_FILE = Schema(
        name_mapping={
            "payload_id": "id",
            "type": "type",
            "url": ("payload", "url"),
            "content_type": ("payload", "contentType"),
            "url_expiry": ("payload", "urlExpiry"),
            "caption": ("payload", "caption"),
            "name": ("payload", "name"),
        },
        pre_parse=type_checker(value="file", field="type"),
        skip_internal=True
    )

    BASE_MODEL = Schema(
        name_mapping={
            "payload_id": "id",
            "type": "type",
        },
        skip_internal=True
    )

    CONTACTS_PAYLOAD = Schema(
        name_mapping={
            "payload_id": "id",
            "contacts": ("payload", "contacts"),
        },
        skip_internal=True
    )

    PAYLOAD_CONTACT_PHONE = Schema(
        name_mapping={
            "phone": "phone",
            "type": "type",
        },
        skip_internal=True
    )

    PAYLOAD_CONTACT_ORGANIZATION = Schema(
        name_mapping={
            "company": "company",
        },
        skip_internal=True
    )

    PAYLOAD_CONTACT_URL = Schema(
        name_mapping={
            "url": "url",
            "type": "type"
        },
        skip_internal=True
    )

    PAYLOAD_CONTACT_INFORMATION = Schema(
        name_mapping={
            "service": "service",
            "user_id": "user_id"
        },
        skip_internal=True
    )

    PAYLOAD_CONTACT = Schema(
        name_mapping={
            "addresses": "addresses",
            "emails": "emails",
            "ims": "ims",
            "name": "name",
            "org": "org",
            "phones": "phones",
            "urls": "urls",
        },
        skip_internal=True
    )

    PAYLOAD_CONTACT_EMAIL = Schema(
        name_mapping={
            "email": "email",
            "type": "type"
        },
        skip_internal=True
    )
    PAYLOAD_CONTACT_ADDRESS = Schema(
        name_mapping={
            "city": "city",
            "country": "country",
            "country_code": "countryCode",
            "state": "state",
            "street": "street",
            "type": "type",
            "zip": "zip"
        },
        skip_internal=True
    )

    RESPONSE_MESSAGE_PAYLOAD_PAYLOAD = Schema(
        name_mapping={
            "whatsapp_Message_id": "whatsappMessageId",
            "type": "type",
        },
        skip_internal=True
    )

    RESPONSE_MESSAGE_PAYLOAD = Schema(
        name_mapping={
            "id": "id",
            "type": "type",
            "destination": "destination",
            "payload": "payload"
        },
        skip_internal=True
    )

    RESPONSE_MESSAGE = Schema(
        name_mapping={
            "app": "app",
            "timestamp": "timestamp",
            "version": "version",
            "type": "type",
            "payload": "payload"
        },
        skip_internal=True
    )
