import dataclasses
from ..shared import destination as shared_destination
from ..shared import destinationinput as shared_destinationinput
from dataclasses_json import dataclass_json
from fabra import utils
from typing import Optional


@dataclasses.dataclass
class CreateDestinationRequest:
    request: shared_destinationinput.DestinationInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class CreateDestination200ApplicationJSON:
    destination: Optional[shared_destination.Destination] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('destination') }})
    

@dataclasses.dataclass
class CreateDestinationResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_destination_200_application_json_object: Optional[CreateDestination200ApplicationJSON] = dataclasses.field(default=None)
    