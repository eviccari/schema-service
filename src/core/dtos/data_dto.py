from pydantic import BaseModel, Field

class DataEspecialistaDTO (BaseModel):
        
    data : str   =  Field(description= "Mensagem que deve ser validada e traduzida",alias="data")
    schema_validador : str   =  Field(description= "Schema utilizado pelo cerberus para realizar a valiadação dos campos de data",alias="schema_validador")
    schema_tranformador: str   =  Field(description= "Schema utilizado pelo pyjq para tranformar o json do campos data",alias="schema_tranformador")
