from dataclasses import dataclass
from typing import Union, Optional

from waio.factory.models.basic import PayloadBaseModel


@dataclass
class PayloadImage(PayloadBaseModel):
    url: str
    content_type: str
    url_expiry: Union[int, str]
    caption: Optional[str] = None
