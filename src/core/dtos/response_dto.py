
from pydantic import BaseModel, Field

class ResponseDTO (BaseModel):

    error_response : dict = Field(description= "Mensagem de erro",alias="error_response")
    data : dict   =  Field(description= "Mensagem traduzida e validada",alias="data")

        