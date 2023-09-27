# Connection
(*connection*)

## Overview

Operations on connections

### Available Operations

* [get_namespaces](#get_namespaces) - Get all namespaces
* [get_schema](#get_schema) - Get schema for table
* [get_tables](#get_tables) - Get all tables

## get_namespaces

Get all namespaces

### Example Usage

```python
import fabra
from fabra.models import operations, shared

s = fabra.Fabra(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.GetNamespacesRequest(
    connection_id=715190,
)

res = s.connection.get_namespaces(req)

if res.namespaces is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetNamespacesRequest](../../models/operations/getnamespacesrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetNamespacesResponse](../../models/operations/getnamespacesresponse.md)**


## get_schema

Get schema for table

### Example Usage

```python
import fabra
from fabra.models import operations, shared

s = fabra.Fabra(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.GetSchemaRequest(
    connection_id=844266,
    namespace='unde',
    table_name='nulla',
)

res = s.connection.get_schema(req)

if res.get_schema_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetSchemaRequest](../../models/operations/getschemarequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetSchemaResponse](../../models/operations/getschemaresponse.md)**


## get_tables

Get all tables

### Example Usage

```python
import fabra
from fabra.models import operations, shared

s = fabra.Fabra(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.GetTablesRequest(
    connection_id=544883,
    namespace='illum',
)

res = s.connection.get_tables(req)

if res.get_tables_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetTablesRequest](../../models/operations/gettablesrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetTablesResponse](../../models/operations/gettablesresponse.md)**

