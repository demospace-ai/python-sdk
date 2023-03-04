from __future__ import annotations
import dataclasses
import requests
from ..shared import source as shared_source
from dataclasses_json import Undefined, dataclass_json
from fabra import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSources200ApplicationJSON:
    sources: Optional[list[shared_source.Source]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sources'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetSourcesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_sources_200_application_json_object: Optional[GetSources200ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    