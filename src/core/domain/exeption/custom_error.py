
from src.core.domain.error_type import ErrorType

class CustomError (Exception):
	
    def __init__(self, message, errorType : ErrorType,idservico) -> None:
        super().__init__(message)
        self.error_type = errorType 
        self.id_servico = idservico

