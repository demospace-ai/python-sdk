import dataclasses
from dataclasses_json import dataclass_json
from fabra import utils


@dataclass_json
@dataclasses.dataclass
class SnowflakeConfig:
    database_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('database_name') }})
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('host') }})
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('password') }})
    role: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('role') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('username') }})
    warehouse_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('warehouse_name') }})
    