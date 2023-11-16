import logging

from fastapi import HTTPException
from src.core.dtos.data_dto import DataEspecialistaDTO
from src.core.dtos.error_dto import ErrorResponseDto
from src.core.dtos.response_dto import ResponseDTO
from src.core.domain.exeption.custom_error import CustomError
from src.core.usecases.tranformar_data import TranformarDataUseCase
from src.entrypoints.http_error_parser import HttpErrorParser


class TransformarDataEntryPoint:
    use_case : TranformarDataUseCase
    entrypoint_nameame : str
    logger : logging

    def __init__(self,use_case : TranformarDataUseCase,entrypoint : str, log : logging) -> None:
        self.use_case = use_case
        self.entrypoint_nameame = entrypoint
        self.logger = log

    def handler(self, data_dto : DataEspecialistaDTO) -> ResponseDTO :
        try:
            self.logger.info("Iniciando transformação de data")
            response = self.use_case.execute(data_dto)
            self.logger.info("Execução finalizada com sucesso")
        except CustomError as c:
            http_status_code = HttpErrorParser.parse(c.error_type.error_name)
            errorResponse = ErrorResponseDto(c,http_status_code)
            self.logger.error(f"Erro na tranformação de data. {errorResponse}")
            raise HTTPException(status_code=http_status_code, detail=errorResponse.__dict__)
        return response