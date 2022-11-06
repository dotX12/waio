from typing import Generator
from typing import Tuple

from aiohttp import FormData
from typing import Any, Optional, Dict


class CustomFormDataStorage(FormData):
    def add_www_form(self, name: str, value: Any):
        self.add_field(name=name, value=value)

    def add_multipart_form(
        self,
        name: str,
        filename: Optional[str],
        value: Any,
        content_type: Optional[str] = None,
    ):
        self.add_field(
            name=name, filename=filename, value=value, content_type=content_type
        )


class CustomFormData(CustomFormDataStorage):
    async def upload(self, key, value: str):
        if isinstance(value, str):
            self.add_www_form(name=key, value=value)

    async def uploads(self, elements: Dict[str, Any]):
        if isinstance(elements, dict):
            for key, value in elements.items():
                await self.upload(key=key, value=value)

    def __iter__(self) -> Generator[Tuple, Any, None]:
        data = self.__dict__.get("_fields")
        for element in data:
            yield element[0]["name"], element[2]
