from __future__ import annotations
import dataclasses
from ..shared import connection as shared_connection
from dataclasses_json import Undefined, dataclass_json
from fabra import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Source:
    connection: Optional[shared_connection.Connection] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('connection'), 'exclude': lambda f: f is None }})
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('display_name'), 'exclude': lambda f: f is None }})
    end_customer_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('end_customer_id'), 'exclude': lambda f: f is None }})
    id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    