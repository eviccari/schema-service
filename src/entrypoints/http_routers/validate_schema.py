from ast import match_case
from re import Match
from fastapi import APIRouter, HTTPException, Response

from src.core.exceptions.application_exception import ApplicationException
from ...core.usecases.validate_schema import ValidateSchema
from ...core.dtos.input_dto import Input


router = APIRouter()
path = "/api/v1"


@router.post(path=f"{path}/validate", response_model=None)
def validate_schema(input: dict, response: Response):
    try:
        result = ValidateSchema().execute(bind_input(input))
        if result.with_error:
            response.status_code = 422
        return {
            "with_errors": result.with_error,
            "errors": result.errors,
        }
    except ApplicationException as ex:
        handle_error(ex=ex)


def bind_input(request_input: dict) -> Input:
    json_schema = request_input.get("json_schema")
    json_body = request_input.get("json_body")
    return Input(
        json_schema=json_schema if json_schema else "",
        json_body=json_body if json_body else ""
    )


def handle_error(ex: ApplicationException) -> None:
    status_code = 500
    match ex.error_type():
        case "BUSINESS_EXCEPTION":
            status_code = 422
        case "PARAMETER_ERROR":
            status_code = 400
        case "TECHNICAL_ERROR":
            status_code = 500
    raise HTTPException(
        status_code=status_code,
        detail=ex.message
    )
