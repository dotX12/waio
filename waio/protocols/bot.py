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

    async def send_file(
        self,
        receiver: int,
        url: str,
        filename: str,
        caption: Optional[str] = None,
    ):
        """Send file message"""

    async def send_video(
        self,
        receiver: int,
        url: str,
        caption: Optional[str] = None,
    ):
        """Send video message"""

    async def send_audio(
        self,
        receiver: int,
        url: str,
    ):
        """Send audio message"""

    async def send_sticker(
        self,
        receiver: int,
        url: str,
    ):
        """Send sticker message"""
