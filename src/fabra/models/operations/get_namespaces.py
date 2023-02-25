from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from fabra import utils
from typing import Optional


@dataclasses.dataclass
class GetNamespacesQueryParams:
    connection_id: int = dataclasses.field(metadata={'query_param': { 'field_name': 'connectionID', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetNamespacesRequest:
    query_params: GetNamespacesQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetNamespaces200ApplicationJSON:
    namespaces: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('namespaces'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetNamespacesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_namespaces_200_application_json_object: Optional[GetNamespaces200ApplicationJSON] = dataclasses.field(default=None)
    