import sys
from loguru import logger
from waio.logs.log_level import loguru_filter

logger.remove()
logger.add(sys.stderr, enqueue=True, filter=loguru_filter, level=0)
