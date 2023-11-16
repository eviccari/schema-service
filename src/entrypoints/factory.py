

from src.core.dtos.response_dto import ResponseDTO
from src.core.usecases.tranformar_data import TranformarDataUseCase
from src.entrypoints.trasformar_data import TransformarDataEntryPoint
from src.infra.factory import Factory as FactoryLog


class Factory():

    @classmethod
    def build_transformar_data(cls) -> TransformarDataEntryPoint:
        usecase = TranformarDataUseCase()
        log = FactoryLog.build_logger()
        log.info("Serviço iniciado com sucesso, Construindo Entrypoints")
        entrypoint = TransformarDataEntryPoint(use_case=usecase,entrypoint="Transformar Data",log=log)
        return entrypoint
