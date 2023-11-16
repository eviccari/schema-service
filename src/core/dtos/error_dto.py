from pydantic import BaseModel, Field

from src.core.domain.error_type import ErrorType
from src.core.domain.exeption.custom_error import CustomError

class ErrorResponseDto (BaseModel) :

	def __init__(self,custom_error : CustomError,http_Status : int):
		dic = {'original_error_code':http_Status,'error_type':custom_error.error_type.error_name,'error_code':http_Status,'error_message':str(custom_error),'mensagem_operador':'Erro na transformação da mensagem, contatar o suporte !','ocorreu':True,'id_servico':custom_error.id_servico}
		super().__init__(**dic)

	original_error_code : int   =  Field(description= "Codigo http do erro original",alias="original_error_code")  
	error_type :        str  =  Field(description= "Typo de erro",alias="error_type")
	error_code  :       int   =  Field(description= "Codigo do erro traduzido",alias="error_code")  
	error_message :     str  =  Field(description= "Mensagem de erro",alias="error_message")
	mensagem_operador:  str  =  Field(description= "Mensagem ao operador de direcionamento ao ocorrer o erro",alias="mensagem_operador") 
	ocorreu  :         bool  =  Field(description= "Se o erro ocorreu",alias="ocorreu") 
	id_servico :        str  =  Field(description= "Id do serviço que gerou o erro",alias="id_servico") 
 