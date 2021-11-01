from dataclasses import dataclass
from typing import Optional

from waio.factory.models.basic import PayloadBaseModel


@dataclass
class PayloadButtonReply(PayloadBaseModel):
    title: Optional[str] = None
    reply: Optional[str] = None
    id: Optional[str] = None
