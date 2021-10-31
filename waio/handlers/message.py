import logging
from typing import List, Any, Optional, Dict, Union

from waio.storage.redis import RedisStorage
from waio.utils.regex import RegexRule

logger = logging.getLogger(__name__)
logging.basicConfig()
logger.setLevel(logging.DEBUG)


class HandlerStorage:

    @staticmethod
    def filter_message_handler(
        handler: dict,
        event: Any,
        user_state: str
    ) -> Optional[Dict[str, Any]]:

        try:
            if event['type'] == 'message':
                hash_handler = hash(handler['function'])
                user = event['payload']['source']
                event_message = event['payload']['payload']['text']
                filters: Dict[str, Union[List[str], Dict[str, Any]]] = handler['filters']
                logger.debug(f"DEBUG - {hash_handler=}")
                logger.debug(f"DEBUG - {user=}")
                logger.debug(f"DEBUG - {event_message=}")
                logger.debug(f"DEBUG - {user_state=}")
                logger.debug(f"DEBUG - {filters.items()}")
                logger.debug(f"===========")

                hitting_filters = {i: False for i in filters.keys()}
                regex_check = None

                for _filter, value in filters.items():
                    print(_filter, value)

                    if _filter == "state":
                        if user_state == str(value):
                            hitting_filters["state"] = True

                    if _filter == 'commands':
                        for filter_value in value:
                            if filter_value == event_message:
                                hitting_filters["commands"] = True

                    if _filter == 'regexp':
                        regex_pattern = RegexRule(regexp=value)
                        regex_check = regex_pattern.check(text=event_message)
                        if regex_check:
                            hitting_filters["regexp"] = True

                if not filters:
                    return {"handler": handler, "event": event}

                elif all(hitting_filters.values()):
                    return {"handler": handler, "event": event, "regex": regex_check}
                else:
                    return None

        except Exception as e:
            raise e

    @staticmethod
    async def debug_filter_message_handler(
        handler: dict,
        event: Any,
        storage: RedisStorage
    ):

        filters: Dict[str, Union[List[str], Dict[str, Any]]] = handler['filters']

        for _filter, value in filters.items():

            print(_filter)
