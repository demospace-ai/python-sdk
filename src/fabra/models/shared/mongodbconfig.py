import dataclasses
from dataclasses_json import dataclass_json
from fabra import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class MongoDbConfig:
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('host') }})
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('password') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('username') }})
    connection_options: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('connection_options') }})
    