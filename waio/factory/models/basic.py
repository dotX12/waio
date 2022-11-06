from dataclasses import dataclass


@dataclass
class PayloadSender:
    phone: int
    name: str


@dataclass
class PayloadBaseModel:
    sender: PayloadSender
    payload_id: str
