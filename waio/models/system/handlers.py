from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import Optional

from waio.handlers import FromFuncHandler


@dataclass
class ExecutedHandlerData:
    handler: Optional[FromFuncHandler] = field(default=None)
    response: Optional[Dict[str, Any]] = field(default=None)
