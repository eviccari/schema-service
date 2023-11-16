from ..domain.validation_result import ValidationResult
from ..domain.schema import Schema
from ..exceptions.business_exception import BusinessException
from ..exceptions.parameter_exception import ParameterException
from ..dtos.input_dto import Input


class ValidateSchema:

    def execute(self, input: Input) -> ValidationResult:
        try:
            if not input.json_schema:
                raise ParameterException("json_schema is required")
            if not input.json_body:
                raise ParameterException("json_body is required")
            s = Schema(input.json_schema)
            return s.validate(json_body=input.json_body)
        except ValueError as error:
            raise BusinessException(
                message=self.__get_errors_from(args=error.args)
            )

    def __get_errors_from(self, args: tuple) -> str:
        error_messages = []
        if not args:
            return ""
        for arg in args:
            if hasattr(arg, "args"):
                error_messages.append(self.__get_errors_from(arg.args))
            else:
                error_messages.append(f"{str(arg)}")
                break
        return ";".join(error_messages)
