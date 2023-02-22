import dataclasses
from ..shared import fieldmapping as shared_fieldmapping
from ..shared import frequencyunits_enum as shared_frequencyunits_enum
from dataclasses_json import dataclass_json
from fabra import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class Sync:
    cursor_field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('cursor_field') }})
    custom_join: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('custom_join') }})
    destination_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('destination_id') }})
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('display_name') }})
    field_mappings: Optional[list[shared_fieldmapping.FieldMapping]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('field_mappings') }})
    frequency: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('frequency') }})
    frequency_units: Optional[shared_frequencyunits_enum.FrequencyUnitsEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('frequency_units') }})
    id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    namespace: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('namespace') }})
    object_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('object_id') }})
    primary_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('primary_key') }})
    source_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('source_id') }})
    table_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('table_name') }})
    