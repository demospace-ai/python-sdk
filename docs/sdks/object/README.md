# Object
(*object*)

## Overview

Operations on objects

### Available Operations

* [create_object](#create_object) - Create a new object
* [get_objects](#get_objects) - Get all objects

## create_object

Create a new object

### Example Usage

```python
import fabra
from fabra.models import shared

s = fabra.Fabra(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.ObjectInput(
    cursor_field='updated_at',
    destination_id=2,
    display_name='BigQuery',
    end_customer_id_field='end_customer_id',
    frequency=30,
    frequency_units=shared.FrequencyUnits.MINUTES,
    namespace='bigquery_dataset',
    object_fields=[
        shared.ObjectField(
            name='event_name',
        ),
    ],
    primary_key='event_id',
    table_name='events',
)

res = s.object.create_object(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `request`                                                | [shared.ObjectInput](../../models/shared/objectinput.md) | :heavy_check_mark:                                       | The request object to use for the request.               |


### Response

**[operations.CreateObjectResponse](../../models/operations/createobjectresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_objects

Get all objects

### Example Usage

```python
import fabra

s = fabra.Fabra(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.object.get_objects()

if res.object is not None:
    # handle response
    pass
```


### Response

**[operations.GetObjectsResponse](../../models/operations/getobjectsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
