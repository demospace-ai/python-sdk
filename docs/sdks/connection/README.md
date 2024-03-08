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
from fabra.models import operations

s = fabra.Fabra(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetNamespacesRequest(
    connection_id=995455,
)

res = s.connection.get_namespaces(req)

if res.namespaces is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetNamespacesRequest](../../models/operations/getnamespacesrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetNamespacesResponse](../../models/operations/getnamespacesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_schema

Get schema for table

### Example Usage

```python
import fabra
from fabra.models import operations

s = fabra.Fabra(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetSchemaRequest(
    connection_id=367941,
    namespace='<value>',
    table_name='<value>',
)

res = s.connection.get_schema(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetSchemaRequest](../../models/operations/getschemarequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetSchemaResponse](../../models/operations/getschemaresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_tables

Get all tables

### Example Usage

```python
import fabra
from fabra.models import operations

s = fabra.Fabra(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetTablesRequest(
    connection_id=820803,
    namespace='<value>',
)

res = s.connection.get_tables(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetTablesRequest](../../models/operations/gettablesrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetTablesResponse](../../models/operations/gettablesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
