from dataclasses import dataclass
from typing import Optional

from waio.factory.models.image import PayloadImage


@dataclass
class PayloadFile(PayloadImage):
    caption: Optional[str] = None
    name: Optional[str] = None
