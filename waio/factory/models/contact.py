from dataclasses import dataclass
from typing import List, Optional, Union


@dataclass
class PayloadSender:
    phone: int
    name: str


@dataclass
class BaseModel:
    sender: PayloadSender
    payload_id: str


@dataclass
class PayloadContactName:
    first_name: str
    formatted_name: str
    last_name: Optional[str] = None


@dataclass
class PayloadContactPhone:
    phone: Optional[str] = None
    type: Optional[str] = None


@dataclass
class PayloadContactAddress:
    city: Optional[str] = None
    country: Optional[str] = None
    country_code: Optional[str] = None
    state: Optional[str] = None
    street: Optional[str] = None
    type: Optional[str] = None
    zip: Optional[str] = None


@dataclass
class PayloadContactEmail:
    email: Optional[str] = None
    type: Optional[str] = None


@dataclass
class PayloadContactOrganization:
    company: Union[str] = None


@dataclass
class PayloadContactUrl:
    url: Optional[str] = None
    type: Optional[str] = None


@dataclass
class PayloadContactInformation:
    service: Optional[str] = None
    user_id: Optional[str] = None


@dataclass
class PayloadContact:
    emails: Optional[List[PayloadContactEmail]] = None
    ims: Optional[List[PayloadContactInformation]] = None
    name: Optional[PayloadContactName] = None
    org: Optional[PayloadContactOrganization] = None
    phones: Optional[List[PayloadContactPhone]] = None
    urls: Optional[List[PayloadContactUrl]] = None
    addresses: Optional[List[PayloadContactAddress]] = None


@dataclass
class PayloadContacts(BaseModel):
    contacts: List[PayloadContact]
