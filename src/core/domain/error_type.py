class ErrorType :
	error_name: str

	def __init__(self,error_name) :
		self.error_name = error_name

TechnicalError = ErrorType("TECHNICAL_ERROR")
BusinessError  = ErrorType("BUSINESS_ERROR")