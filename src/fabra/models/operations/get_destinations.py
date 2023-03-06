from __future__ import annotations
import dataclasses
import requests
from ..shared import destination as shared_destination
from dataclasses_json import Undefined, dataclass_json
from fabra import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDestinations200ApplicationJSON:
    destinations: Optional[list[shared_destination.Destination]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinations'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetDestinationsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_destinations_200_application_json_object: Optional[GetDestinations200ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    