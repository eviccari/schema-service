import pytest
from .schema import Schema

def test_should_validate_schema_with_success():
    json_schema = "{\"name\": {\"type\": \"string\", \"max\": 10}}"
    json_payload = "{\"name\": \"Tester\"}"
    s = Schema(json_schema=json_schema)
    result = s.validate(json_body=json_payload)
    assert result.with_error is False


def test_should_validate_schema_with_errors():
    json_schema = "{\"name\": {\"type\": \"string\", \"max\": 10}, \"age\": {\"type\": \"integer\", \"min\": 1, \"max\": 200}}"
    json_payload = "{\"name\": \"Tester\", \"age\": 0}"
    s = Schema(json_schema=json_schema)
    result = s.validate(json_body=json_payload)
    assert result.with_error is True


def test_should_rise_value_error_when_convert_invalid_json():
    json_schema = "{\"name\": {\"type\": \"string\", \"max\": 10}, \"age\": {\"type\": \"integer\", \"min\": 1, \"max\": 200}}"
    invalid_json_payload = "{\"name\": \"Tester\","    
    s = Schema(json_schema=json_schema)
    with pytest.raises(ValueError):
        s.validate(invalid_json_payload)




     
