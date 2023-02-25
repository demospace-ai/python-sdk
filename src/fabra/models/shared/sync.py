from __future__ import annotations
import dataclasses
from ..shared import fieldmapping as shared_fieldmapping
from ..shared import frequencyunits_enum as shared_frequencyunits_enum
from dataclasses_json import Undefined, dataclass_json
from fabra import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Sync:
    cursor_field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('cursor_field'), 'exclude': lambda f: f is None }})
    custom_join: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('custom_join'), 'exclude': lambda f: f is None }})
    destination_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('destination_id'), 'exclude': lambda f: f is None }})
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('display_name'), 'exclude': lambda f: f is None }})
    field_mappings: Optional[list[shared_fieldmapping.FieldMapping]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('field_mappings'), 'exclude': lambda f: f is None }})
    frequency: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('frequency'), 'exclude': lambda f: f is None }})
    frequency_units: Optional[shared_frequencyunits_enum.FrequencyUnitsEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('frequency_units'), 'exclude': lambda f: f is None }})
    id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    namespace: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('namespace'), 'exclude': lambda f: f is None }})
    object_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('object_id'), 'exclude': lambda f: f is None }})
    primary_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('primary_key'), 'exclude': lambda f: f is None }})
    source_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('source_id'), 'exclude': lambda f: f is None }})
    table_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('table_name'), 'exclude': lambda f: f is None }})
    