from typing import Dict, Any


class ExampleDatabase:
    def __init__(self):
        self.session: str = "CLOSED"
        self.data: Dict[str, Any] = {}

    def open_session(self) -> None:
        self.session = 'OPEN'

    def close_session(self) -> None:
        self.session = 'CLOSED'

    @property
    def connection(self) -> bool:
        if self.session == 'CLOSED':
            raise Exception('Database is closed...')
        return True

    def set(self, key, value) -> None:
        if self.connection:
            self.data[key] = value

    def get(self, key) -> Any:
        if self.connection:
            return self.data[key]
