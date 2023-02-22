import dataclasses
from ..shared import fieldmapping as shared_fieldmapping
from ..shared import frequencyunits_enum as shared_frequencyunits_enum
from dataclasses_json import dataclass_json
from fabra import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class SyncInput:
    destination_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('destination_id') }})
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('display_name') }})
    field_mappings: list[shared_fieldmapping.FieldMapping] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('field_mappings') }})
    frequency: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('frequency') }})
    frequency_units: shared_frequencyunits_enum.FrequencyUnitsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('frequency_units') }})
    object_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('object_id') }})
    source_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('source_id') }})
    cursor_field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('cursor_field') }})
    custom_join: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('custom_join') }})
    namespace: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('namespace') }})
    primary_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('primary_key') }})
    table_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('table_name') }})
    