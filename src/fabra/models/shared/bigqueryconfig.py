from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from fabra import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BigQueryConfig:
    location: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location') }})
    credentials: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    