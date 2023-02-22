import dataclasses
from ..shared import object as shared_object
from ..shared import objectinput as shared_objectinput
from dataclasses_json import dataclass_json
from fabra import utils
from typing import Optional


@dataclasses.dataclass
class CreateObjectRequest:
    request: shared_objectinput.ObjectInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class CreateObject200ApplicationJSON:
    object: Optional[shared_object.Object] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('object') }})
    

@dataclasses.dataclass
class CreateObjectResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_object_200_application_json_object: Optional[CreateObject200ApplicationJSON] = dataclasses.field(default=None)
    