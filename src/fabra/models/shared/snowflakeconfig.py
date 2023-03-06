from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from fabra import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SnowflakeConfig:
    database_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database_name') }})
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    role: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    warehouse_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warehouse_name') }})
    