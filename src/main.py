from fastapi import FastAPI
from src.core.dtos.data_dto import DataEspecialistaDTO
from src.core.dtos.response_dto import ResponseDTO
from src.entrypoints.factory import Factory
from src.config.configuration import Configuration

app = FastAPI(title="HUB_DE_OFERTAS_TRANFORMADOR",description="descrição do projeto")
Configuration().read()
entry = Factory.build_transformar_data()


@app.post("/api/v1/transformar")
def index(data_dto: DataEspecialistaDTO) -> ResponseDTO:
    return entry.handler(data_dto)
