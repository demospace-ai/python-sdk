from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import sync as shared_sync
from ..shared import syncinput as shared_syncinput
from dataclasses_json import Undefined, dataclass_json
from fabra import utils
from typing import Optional


@dataclasses.dataclass
class CreateSyncRequest:
    request: shared_syncinput.SyncInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateSync200ApplicationJSON:
    sync: Optional[shared_sync.Sync] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sync'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class CreateSyncResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_sync_200_application_json_object: Optional[CreateSync200ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    