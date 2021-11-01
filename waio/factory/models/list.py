from dataclasses import dataclass
from typing import Optional

from waio.factory.models.basic import PayloadBaseModel


@dataclass
class PayloadList(PayloadBaseModel):
    title: Optional[str]
    id: Optional[str] = None
    reply: Optional[str] = None
    postback_text: Optional[str] = None
    description: Optional[str] = None
