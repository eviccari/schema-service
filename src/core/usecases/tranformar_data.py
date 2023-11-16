

import json
from src.core.dtos.data_dto import DataEspecialistaDTO
from src.core.dtos.error_dto import ErrorResponseDto
from src.core.dtos.response_dto import ResponseDTO
from src.core.domain.data import DataEspecialista
from src.core.domain.error_type import BusinessError
from src.core.domain.exeption.custom_error import CustomError
from src.core.domain.factory import ModelFactory
from cerberus import Validator

class TranformarDataUseCase():

    validator : Validator

    def __init__(self) -> None:
        self.validator = Validator()

    def execute(self,data_dto : DataEspecialistaDTO) -> ResponseDTO:
        try:
            request_data = ModelFactory().buil_data_from_dto(data_dto)
            data = DataEspecialista(request_data)
            data.validar_parametros()
            schema = json.loads(data.schema_validador)
            data = json.loads(data.data)
            if not self.validator(data,schema):
                raise ValueError(self.validator.errors)
            return ResponseDTO(error_response={},data=data)
        except ValueError as e:
            raise CustomError(str(e),BusinessError,"")
        


        

