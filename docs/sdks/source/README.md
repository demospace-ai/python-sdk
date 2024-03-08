# Source
(*source*)

## Overview

Operations on sources

### Available Operations

* [create_source](#create_source) - Create a new source
* [get_sources](#get_sources) - Get all sources

## create_source

Create a new source

### Example Usage

```python
import fabra
from fabra.models import shared

s = fabra.Fabra(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.SourceInput(
    connection_type=shared.ConnectionType.WEBHOOK,
    display_name='Frontend Events',
    end_customer_id='abcd-1234-efgh-5678',
)

res = s.source.create_source(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `request`                                                | [shared.SourceInput](../../models/shared/sourceinput.md) | :heavy_check_mark:                                       | The request object to use for the request.               |


### Response

**[operations.CreateSourceResponse](../../models/operations/createsourceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_sources

Get all sources

### Example Usage

```python
import fabra

s = fabra.Fabra(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.source.get_sources()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetSourcesResponse](../../models/operations/getsourcesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
