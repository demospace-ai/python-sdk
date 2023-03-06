from __future__ import annotations
from enum import Enum

class FrequencyUnitsEnum(str, Enum):
    MINUTES = "minutes"
    HOURS = "hours"
    DAYS = "days"
    WEEKS = "weeks"
