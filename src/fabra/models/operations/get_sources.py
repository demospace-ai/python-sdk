import dataclasses
from ..shared import source as shared_source
from dataclasses_json import dataclass_json
from fabra import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class GetSources200ApplicationJSON:
    sources: Optional[list[shared_source.Source]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sources') }})
    

@dataclasses.dataclass
class GetSourcesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_sources_200_application_json_object: Optional[GetSources200ApplicationJSON] = dataclasses.field(default=None)
    