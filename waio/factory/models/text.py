from dataclasses import dataclass

from waio.factory.models.basic import PayloadBaseModel


@dataclass
class PayloadText(PayloadBaseModel):
    text: str
