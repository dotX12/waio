from typing import Any
from typing import Optional

from waio.client.http import HTTPClient
from waio.gupshup.api import GupshupSettings
from waio.gupshup.form import generate_message_form
from waio.keyboard.list import ListMessage
from waio.keyboard.reply import QuickReply
from waio.models.audio import AudioModel
from waio.models.enums import GupshupMethods
from waio.models.file import FileModel
from waio.models.image import ImageModel
from waio.models.sticker import StickerModel
from waio.models.text import MessageText
from waio.models.video import VideoModel
from waio.utils.form_data import CustomFormData


class Bot(GupshupSettings, HTTPClient):
    def __init__(self, apikey: str, src_name: str, phone_number: int):
        super().__init__(apikey=apikey, src_name=src_name, phone_number=phone_number)

    async def _base_request(self, receiver: int, data: Any):
        form = self._generate_form(receiver=receiver, data=data)
        response = await self.request(
            headers=self._headers(),
            method="POST",
            url=str(GupshupMethods.message.value),
            data=form,
        )
        return response

    def _generate_form(self, receiver, data) -> CustomFormData:
        return generate_message_form(
            source=self.phone_number,
            receiver=receiver,
            app_name=self.src_name,
            message=data.json(),
        )

    async def send_message(self, receiver: int, message: str):
        msg = MessageText(text=message)
        return await self._base_request(receiver=receiver, data=msg)

    async def send_image(
        self,
        receiver: int,
        original_url: str,
        preview_url: Optional[str] = None,
        caption: Optional[str] = None,
    ):
        image = ImageModel(
            original_url=original_url, preview_url=preview_url, caption=caption
        )
        return await self._base_request(receiver=receiver, data=image)

    async def send_file(
        self,
        receiver: int,
        url: str,
        filename: str,
        caption: Optional[str] = None,
    ):
        file = FileModel(url=url, filename=filename, caption=caption)
        return await self._base_request(receiver=receiver, data=file)

    async def send_video(
        self,
        receiver: int,
        url: str,
        caption: Optional[str] = None,
    ):
        video = VideoModel(url=url, caption=caption)
        return await self._base_request(receiver=receiver, data=video)

    async def send_audio(
        self,
        receiver: int,
        url: str,
    ):
        audio = AudioModel(url=url)
        return await self._base_request(receiver=receiver, data=audio)

    async def send_sticker(
        self,
        receiver: int,
        url: str,
    ):
        sticker = StickerModel(url=url)
        return await self._base_request(receiver=receiver, data=sticker)

    async def send_list(self, receiver: int, keyboard: ListMessage):
        return await self._base_request(receiver=receiver, data=keyboard)

    async def send_reply(self, receiver: int, keyboard: QuickReply):
        return await self._base_request(receiver=receiver, data=keyboard)
