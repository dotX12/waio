from aiohttp import FormData
from typing import Any, Optional, Dict, Union
from fastapi import UploadFile


class CustomFormDataStorage(FormData):
    def add_www_form(self, name: str, value: Any):
        self.add_field(name=name, value=value)

    def add_multipart_form(self, name: str, filename: Optional[str], value: Any, content_type: Optional[str] = None):
        self.add_field(name=name, filename=filename, value=value, content_type=content_type)


class CustomFormData(CustomFormDataStorage):
    async def upload(self, key, value: Union[UploadFile, str]):
        if isinstance(value, UploadFile):
            bytes_file = await value.read()
            self.add_multipart_form(
                name=key, filename=value.filename, value=bytes_file, content_type=value.content_type)
        elif isinstance(value, str):
            self.add_www_form(name=key, value=value)

    async def uploads(self, elements: Dict[str, Any]):
        if isinstance(elements, dict):
            for key, value in elements.items():
                await self.upload(key=key, value=value)

    def __iter__(self):
        data = self.__dict__.get('_fields')
        for element in data:
            yield element[0]['name'], element[2]
