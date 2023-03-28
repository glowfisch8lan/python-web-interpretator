from jsonschema import validate as validator_validate

from src.base.exceptions.ValidationException import ValidationException


def validate(data, schema):
    try:
        validator_validate(instance=data, schema=schema)
    except:
        raise ValidationException()
