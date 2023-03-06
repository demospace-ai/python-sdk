from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createlinktokenrequest as shared_createlinktokenrequest
from ..shared import createlinktokenresponse as shared_createlinktokenresponse
from typing import Optional


@dataclasses.dataclass
class CreateLinkTokenRequest:
    request: shared_createlinktokenrequest.CreateLinkTokenRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateLinkTokenResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_link_token_response: Optional[shared_createlinktokenresponse.CreateLinkTokenResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    