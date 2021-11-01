from typing import Protocol


class Bot(Protocol):

    async def send_message(self, receiver: int, message: str):
        """Send message"""
