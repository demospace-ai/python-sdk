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
from fabra.models import components

s = fabra.Fabra(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.object.create_object(request=components.ObjectInput(
    destination_id=2,
    display_name='BigQuery',
    end_customer_id_field='end_customer_id',
    frequency=30,
    frequency_units=components.FrequencyUnits.MINUTES,
    namespace='bigquery_dataset',
    table_name='events',
    cursor_field='updated_at',
    object_fields=[
        components.ObjectField(
            name='event_name',
        ),
    ],
    primary_key='event_id',
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [components.ObjectInput](../../models/components/objectinput.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.CreateObjectResponse](../../models/operations/createobjectresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

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
| errors.SDKError | 4xx-5xx         | */*             |
