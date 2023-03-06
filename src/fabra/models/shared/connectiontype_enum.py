from __future__ import annotations
from enum import Enum

class ConnectionTypeEnum(str, Enum):
    SNOWFLAKE = "snowflake"
    BIGQUERY = "bigquery"
    REDSHIFT = "redshift"
    MONGODB = "mongodb"
    WEBHOOK = "webhook"
