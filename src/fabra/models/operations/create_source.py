from __future__ import annotations
import dataclasses
from ..shared import source as shared_source
from ..shared import sourceinput as shared_sourceinput
from dataclasses_json import Undefined, dataclass_json
from fabra import utils
from typing import Optional


@dataclasses.dataclass
class CreateSourceRequest:
    request: shared_sourceinput.SourceInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateSource200ApplicationJSON:
    source: Optional[shared_source.Source] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('source'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class CreateSourceResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_source_200_application_json_object: Optional[CreateSource200ApplicationJSON] = dataclasses.field(default=None)
    