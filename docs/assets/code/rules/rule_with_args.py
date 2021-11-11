from typing import Dict, Union, Tuple
from phonenumbers import timezone, parse, geocoder

from waio.rules import ABCRule
from waio.types import Message

G_T: Dict[str, Union[int, str, Tuple[str]]]


class RussianNumberRule(ABCRule):
    async def check(self, message: Message) -> Union[bool, G_T]:
        phone_number_data = self.get_phone_number_data(message.sender_number)
        if phone_number_data["country"] == "Russia":
            return phone_number_data
        return False

    @staticmethod
    def get_phone_number_data(number: str) -> G_T:
        phone_number = parse(number)
        country_name = geocoder.country_name_for_number(phone_number, "en")
        time_zones_number = timezone.time_zones_for_number(phone_number)

        return {
            "country_code": phone_number.country_code,
            "national_number": phone_number.national_number,
            "country": country_name,
            "time_zone": time_zones_number
        }
