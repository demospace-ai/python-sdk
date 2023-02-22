import dataclasses
from enum import Enum

class FieldTypeEnum(str, Enum):
    STRING = "string"
    INTEGER = "integer"
    TIMESTAMP = "timestamp"
    JSON = "json"
    BOOLEAN = "boolean"
