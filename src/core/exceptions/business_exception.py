from .application_exception import ApplicationException


class BusinessException(ApplicationException):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    def error_type(self) -> str:
        return "BUSINESS_EXCEPTION"