from __future__ import annotations
import dataclasses
from ..shared import objectfield as shared_objectfield
from dataclasses_json import Undefined, dataclass_json
from fabra import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Object:
    destination_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destination_id'), 'exclude': lambda f: f is None }})
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display_name'), 'exclude': lambda f: f is None }})
    end_customer_id_field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_customer_id_field'), 'exclude': lambda f: f is None }})
    id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    namespace: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespace'), 'exclude': lambda f: f is None }})
    object_fields: Optional[list[shared_objectfield.ObjectField]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_fields'), 'exclude': lambda f: f is None }})
    table_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('table_name'), 'exclude': lambda f: f is None }})
    