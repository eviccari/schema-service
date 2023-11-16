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
            message = "|".join(error.args)
            raise BusinessException(message=message)

