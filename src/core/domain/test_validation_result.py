from typing import List
from .validation_result import ValidationResult

def test_should_create_validation_result():
    vr = ValidationResult(errors=None)
    assert vr.with_error is False

def test_should_create_validation_result_with_errors():
    errors = [
        {"name": ["must be of type string"]},
        {"age": ["unknown field"]},
    ]
    vr = ValidationResult(errors=errors)
    assert vr.with_error
    assert len(vr.errors) == 2