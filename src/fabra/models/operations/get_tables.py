from __future__ import annotations
import dataclasses
import requests
from dataclasses_json import Undefined, dataclass_json
from fabra import utils
from typing import Optional


@dataclasses.dataclass
class GetTablesQueryParams:
    connection_id: int = dataclasses.field(metadata={'query_param': { 'field_name': 'connectionID', 'style': 'form', 'explode': True }})
    namespace: str = dataclasses.field(metadata={'query_param': { 'field_name': 'namespace', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetTablesRequest:
    query_params: GetTablesQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetTables200ApplicationJSON:
    tables: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tables'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetTablesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_tables_200_application_json_object: Optional[GetTables200ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    