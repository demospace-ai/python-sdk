from __future__ import annotations
import dataclasses
from ..shared import objectfield as shared_objectfield
from dataclasses_json import Undefined, dataclass_json
from fabra import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ObjectInput:
    destination_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destination_id') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display_name') }})
    end_customer_id_field: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_customer_id_field') }})
    namespace: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespace') }})
    table_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('table_name') }})
    object_fields: Optional[list[shared_objectfield.ObjectField]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_fields'), 'exclude': lambda f: f is None }})
    