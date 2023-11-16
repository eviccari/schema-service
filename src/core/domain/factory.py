
import json
from src.core.dtos.data_dto import DataEspecialistaDTO
from src.core.domain.data import DataEspecialista


class ModelFactory :

    def buil_data_from_dto(self,dto : DataEspecialistaDTO) -> DataEspecialista :
        json_string = json.dumps(dto.__dict__)
        obj : DataEspecialista = json.loads(json_string) 
        return obj