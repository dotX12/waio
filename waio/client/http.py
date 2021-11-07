import aiohttp
import ujson

from urllib.parse import unquote
from typing import Optional, Union, Dict, Any, List, Tuple
from aiohttp import ContentTypeError

from waio.client.exceptions import FailedDecodeJson


class HTTPClient:
    async def request(
        self,
        method: str,
        url: str,
        headers: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Tuple[Dict[str, Any], int]:
        if not headers:
            headers = {}

        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.request(method=method, url=url, **kwargs) as resp:
                return await self.generate_json_from_response(resp)

    async def generate_json_from_response(
        self,
        resp: aiohttp.ClientResponse
    ) -> Tuple[Dict[str, Any], int]:
        content_type = resp.headers.get('Content-Type')
        try:
            if content_type == 'text/plain':
                resp_text = await resp.text()
                resp_json = ujson.loads(resp_text)
                return self.decode_json(resp_json), resp.status

            elif content_type == 'application/json':
                resp_json = await resp.json()
                return resp_json, resp.status

        except ContentTypeError as e:
            raise FailedDecodeJson(f"Check args, URL is invalid - {e}")

    @staticmethod
    def decode_json(data: Union[List, Dict[str, Any]]):
        data_dumps = ujson.dumps(data, ensure_ascii=False)
        decoded_data_str = unquote(data_dumps)
        data_data_json = ujson.loads(decoded_data_str)
        return data_data_json

    @staticmethod
    def prepare_url(base_url: str, url: str, **kwargs):
        url = f"{base_url}/{url.format(**kwargs)}"
        return url
