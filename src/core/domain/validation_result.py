from typing import List


class ValidationResult:
    def __init__(self, errors: List[dict] | None) -> None:
        self.__with_error = True if errors else False
        self.__errors = errors

    @property
    def with_error(self) -> bool:
        return self.__with_error

    @property
    def errors(self) -> List[dict]:
        return self.__errors
