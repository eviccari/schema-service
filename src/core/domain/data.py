import json

class DataEspecialista ():
    
    data : str   
    schema_validador : str   
    schema_tranformador: str 
    
    def __init__(self, my_dict): 
            for key in my_dict: 
                setattr(self, key, my_dict[key])

    def validar_parametros(self): 
        if not is_json(self.schema_validador):
            raise ValueError("O schema_validador deve ser um json valido")
        if not is_json(self.schema_tranformador) :
            raise ValueError('o schema_tranformador deve ser um json valido escrito no formato string. Ex "{\"teste\":\"teste\"}"')
        if not is_json(self.data) :
            raise ValueError("o capo data deve ser um json valido")

def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError as e:
        return False
    return True
    