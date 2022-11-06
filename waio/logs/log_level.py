from loguru import logger


class LogFilterLevel:
    def __init__(self, lvl):
        self.level = lvl

    def __call__(self, record) -> bool:
        level_no = logger.level(self.level).no
        return record["level"].no >= level_no

    def set_level(self, lvl):
        self.level = lvl


loguru_filter = LogFilterLevel("WARNING")
