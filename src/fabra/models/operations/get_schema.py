import dataclasses
from ..shared import columnschema as shared_columnschema
from dataclasses_json import dataclass_json
from fabra import utils
from typing import Optional


@dataclasses.dataclass
class GetSchemaQueryParams:
    connection_id: int = dataclasses.field(metadata={'query_param': { 'field_name': 'connectionID', 'style': 'form', 'explode': True }})
    namespace: str = dataclasses.field(metadata={'query_param': { 'field_name': 'namespace', 'style': 'form', 'explode': True }})
    table_name: str = dataclasses.field(metadata={'query_param': { 'field_name': 'table_name', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetSchemaRequest:
    query_params: GetSchemaQueryParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetSchema200ApplicationJSON:
    schema: Optional[list[shared_columnschema.ColumnSchema]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('schema') }})
    

@dataclasses.dataclass
class GetSchemaResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_schema_200_application_json_object: Optional[GetSchema200ApplicationJSON] = dataclasses.field(default=None)
    