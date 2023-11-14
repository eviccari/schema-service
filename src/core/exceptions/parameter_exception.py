from .application_exception import ApplicationException


class ParameterException(ApplicationException):
    def __init__(self, message: str) -> None:
        super().__init__(message)


    def error_type(self) -> str:
        return "PARAMETER_ERROR"