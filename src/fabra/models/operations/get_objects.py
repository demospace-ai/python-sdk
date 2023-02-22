import dataclasses
from ..shared import object as shared_object
from dataclasses_json import dataclass_json
from fabra import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class GetObjects200ApplicationJSON:
    objects: Optional[list[shared_object.Object]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('objects') }})
    

@dataclasses.dataclass
class GetObjectsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_objects_200_application_json_object: Optional[GetObjects200ApplicationJSON] = dataclasses.field(default=None)
    