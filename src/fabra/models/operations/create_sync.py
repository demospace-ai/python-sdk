import dataclasses
from ..shared import sync as shared_sync
from ..shared import syncinput as shared_syncinput
from dataclasses_json import dataclass_json
from fabra import utils
from typing import Optional


@dataclasses.dataclass
class CreateSyncRequest:
    request: shared_syncinput.SyncInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class CreateSync200ApplicationJSON:
    sync: Optional[shared_sync.Sync] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sync') }})
    

@dataclasses.dataclass
class CreateSyncResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_sync_200_application_json_object: Optional[CreateSync200ApplicationJSON] = dataclasses.field(default=None)
    