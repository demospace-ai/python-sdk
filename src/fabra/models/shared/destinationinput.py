import dataclasses
from ..shared import bigqueryconfig as shared_bigqueryconfig
from ..shared import connectiontype_enum as shared_connectiontype_enum
from ..shared import mongodbconfig as shared_mongodbconfig
from ..shared import redshiftconfig as shared_redshiftconfig
from ..shared import snowflakeconfig as shared_snowflakeconfig
from dataclasses_json import dataclass_json
from fabra import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class DestinationInput:
    connection_type: shared_connectiontype_enum.ConnectionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('connection_type') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('display_name') }})
    bigquery_config: Optional[shared_bigqueryconfig.BigQueryConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('bigquery_config') }})
    mongodb_config: Optional[shared_mongodbconfig.MongoDbConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('mongodb_config') }})
    redshift_config: Optional[shared_redshiftconfig.RedshiftConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('redshift_config') }})
    snowflake_config: Optional[shared_snowflakeconfig.SnowflakeConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('snowflake_config') }})
    