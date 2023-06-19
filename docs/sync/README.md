# sync

## Overview

Operations on syncs

### Available Operations

* [create_sync](#create_sync) - Create a new sync
* [get_syncs](#get_syncs) - Get all syncs

## create_sync

Create a new sync

### Example Usage

```python
import fabra
from fabra.models import shared

s = fabra.Fabra(
    security=shared.Security(
        api_key_auth="YOUR_API_KEY_HERE",
    ),
)

req = shared.SyncInput(
    cursor_field='updated_at',
    custom_join='select * from events join additional_properties on events.id = additional_properties.event_id;',
    destination_id=2,
    display_name='Event Sync',
    field_mappings=[
        shared.FieldMapping(
            destination_field_name='event',
            source_field_name='event_name',
        ),
        shared.FieldMapping(
            destination_field_name='event',
            source_field_name='event_name',
        ),
    ],
    frequency=30,
    frequency_units=shared.FrequencyUnitsEnum.HOURS,
    namespace='end_customer_bigquery_dataset',
    object_id=3,
    primary_key='event_id',
    source_id=1,
    table_name='end_customer_events',
)

res = s.sync.create_sync(req)

if res.create_sync_200_application_json_object is not None:
    # handle response
```

## get_syncs

Get all syncs

### Example Usage

```python
import fabra


s = fabra.Fabra(
    security=shared.Security(
        api_key_auth="YOUR_API_KEY_HERE",
    ),
)


res = s.sync.get_syncs()

if res.get_syncs_200_application_json_object is not None:
    # handle response
```
