from .validation_result import ValidationResult
from cerberus import Validator
from ast import literal_eval


class Schema:
    def __init__(self, json_schema: str) -> None:
        self.__json_schema = self.__convert(json_schema)


    @property
    def json_schema(self) -> dict:
        return self.__json_schema
    
    
    def validate(self, json_payload: str) -> ValidationResult:
        v = Validator(self.json_schema)
        v.validate(document=self.__convert(json_payload))
        if v.errors:
            return ValidationResult(errors=v.errors)
        return ValidationResult(errors=None)

        
          
    def __convert(self, string_value: str) -> dict:
        try:
            return literal_eval(string_value)
        except Exception as error:
            raise ValueError(error)

        