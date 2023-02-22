import dataclasses
from ..shared import objectfield as shared_objectfield
from dataclasses_json import dataclass_json
from fabra import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class Object:
    customer_id_column: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('customer_id_column') }})
    destination_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('destination_id') }})
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('display_name') }})
    id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    namespace: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('namespace') }})
    object_fields: Optional[list[shared_objectfield.ObjectField]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('object_fields') }})
    table_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('table_name') }})
    