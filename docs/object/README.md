# object

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
    security=shared.Security(
        api_key_auth="YOUR_API_KEY_HERE",
    ),
)

req = shared.ObjectInput(
    destination_id=2,
    display_name='BigQuery',
    end_customer_id_field='end_customer_id',
    namespace='bigquery_dataset',
    object_fields=[
        shared.ObjectField(
            name='event_name',
            type=shared.FieldTypeEnum.JSON,
        ),
        shared.ObjectField(
            name='event_name',
            type=shared.FieldTypeEnum.JSON,
        ),
    ],
    table_name='events',
)

res = s.object.create_object(req)

if res.create_object_200_application_json_object is not None:
    # handle response
```

## get_objects

Get all objects

### Example Usage

```python
import fabra


s = fabra.Fabra(
    security=shared.Security(
        api_key_auth="YOUR_API_KEY_HERE",
    ),
)


res = s.object.get_objects()

if res.get_objects_200_application_json_object is not None:
    # handle response
```
