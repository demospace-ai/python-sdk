from __future__ import annotations
import dataclasses
import requests
from ..shared import sync as shared_sync
from dataclasses_json import Undefined, dataclass_json
from fabra import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSyncs200ApplicationJSON:
    syncs: Optional[list[shared_sync.Sync]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncs'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetSyncsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_syncs_200_application_json_object: Optional[GetSyncs200ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    