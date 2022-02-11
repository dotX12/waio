from typing import Optional
from typing import Protocol
from waio.keyboard.list import ListMessage
from waio.keyboard.reply import QuickReply


class Bot(Protocol):

    async def send_message(self, receiver: int, message: str):
        """Send message"""

    async def send_list(self, receiver: int, keyboard: ListMessage):
        """Send list message"""

    async def send_reply(self, receiver: int, keyboard: QuickReply):
        """Send reply message"""

    async def send_image(
        self,
        receiver: int,
        original_url: str,
        preview_url: Optional[str] = None,
        caption: Optional[str] = None,
    ):
        """Send image message"""
