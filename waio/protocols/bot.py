from typing import Protocol
from waio.keyboard.list import ListMessage


class Bot(Protocol):

    async def send_message(self, receiver: int, message: str):
        """Send message"""

    async def send_list(self, receiver: int, button: ListMessage):
        """Send list message"""
