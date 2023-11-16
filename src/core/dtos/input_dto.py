class Input:
    def __init__(self, json_schema:str, json_body: str) -> None:
        self.__json_schema = json_schema
        self.__json_body = json_body

    
    @property
    def json_schema(self) -> str:
        return self.__json_schema
    

    @property
    def json_body(self) -> str:
        return self.__json_body