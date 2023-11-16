

from http import HTTPStatus

class HttpErrorParser():

    @classmethod
    def parse(cls,error : str) -> int :
        if error == "TECHNICAL_ERROR":
            return HTTPStatus.INTERNAL_SERVER_ERROR
        elif error == "BUSINESS_ERROR":
            return HTTPStatus.UNPROCESSABLE_ENTITY
        else: 
            return 500