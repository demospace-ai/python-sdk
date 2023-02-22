import dataclasses
from ..shared import objectfield as shared_objectfield
from dataclasses_json import dataclass_json
from fabra import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class ObjectInput:
    customer_id_column: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('customer_id_column') }})
    destination_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('destination_id') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('display_name') }})
    namespace: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('namespace') }})
    table_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('table_name') }})
    object_fields: Optional[list[shared_objectfield.ObjectField]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('object_fields') }})
    