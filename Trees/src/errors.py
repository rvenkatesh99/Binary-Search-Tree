from typing import Any

class MissingValueError(Exception):
    def __init__(self, *args: Any) -> None:
        super().__init__(*args)

class EmptyTreeError(Exception):
    def __init__(self, *args: Any) -> None:
        super().__init__(*args)
