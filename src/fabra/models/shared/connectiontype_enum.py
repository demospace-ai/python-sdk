from __future__ import annotations
import dataclasses
from enum import Enum

class ConnectionTypeEnum(str, Enum):
    SNOWFLAKE = "snowflake"
    BIGQUERY = "bigquery"
    REDSHIFT = "redshift"
    MONGODB = "mongodb"
    WEBHOOK = "webhook"
