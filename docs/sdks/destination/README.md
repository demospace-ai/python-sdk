# Destination
(*destination*)

## Overview

Operations on destinations

### Available Operations

* [create_destination](#create_destination) - Create a new destination
* [get_destinations](#get_destinations) - Get all destinations

## create_destination

Create a new destination

### Example Usage

```python
import fabra
from fabra.models import shared

s = fabra.Fabra(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.DestinationInput(
    connection_type=shared.ConnectionType.SNOWFLAKE,
    display_name='BigQuery',
)

res = s.destination.create_destination(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.DestinationInput](../../models/shared/destinationinput.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.CreateDestinationResponse](../../models/operations/createdestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_destinations

Get all destinations

### Example Usage

```python
import fabra

s = fabra.Fabra(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.destination.get_destinations()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetDestinationsResponse](../../models/operations/getdestinationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
