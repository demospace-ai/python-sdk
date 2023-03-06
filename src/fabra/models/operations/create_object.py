from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import object as shared_object
from ..shared import objectinput as shared_objectinput
from dataclasses_json import Undefined, dataclass_json
from fabra import utils
from typing import Optional


@dataclasses.dataclass
class CreateObjectRequest:
    request: shared_objectinput.ObjectInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateObject200ApplicationJSON:
    object: Optional[shared_object.Object] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class CreateObjectResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_object_200_application_json_object: Optional[CreateObject200ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    