from typing import Dict


class GupshupSettings:
    def __init__(self, apikey: str, src_name: str, phone_number: int):
        self.apikey = apikey
        self.src_name = src_name
        self.phone_number = phone_number

    def _headers(self) -> Dict[str, str]:
        headers = {
            "Cache-Control": "no-cache",
            "cache-control": "no-cache",
            "Content-Type": "application/x-www-form-urlencoded",
            "apikey": self.apikey,
        }
        return headers
