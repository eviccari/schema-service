from abc import ABC, abstractmethod

class ApplicationException(ABC, Exception):
    def __init__(self, message: str) -> None:
        super().__init__()
        self.__message = message
        
    @property
    def message(self) -> str:
        return self.__message
    
    @abstractmethod
    def error_type(self) -> str:
        pass

    