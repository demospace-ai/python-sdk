# Sync
(*.sync*)

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
    api_key_auth="",
)

req = shared.SyncInput(
    cursor_field='updated_at',
    custom_join='select * from events join additional_properties on events.id = additional_properties.event_id;',
    destination_id=2,
    display_name='Event Sync',
    end_customer_id='abc123',
    field_mappings=[
        shared.FieldMapping(
            destination_field_name='event',
            source_field_name='event_name',
        ),
    ],
    frequency=30,
    namespace='end_customer_bigquery_dataset',
    object_id=3,
    primary_key='event_id',
    source_id=1,
    table_name='end_customer_events',
)

res = s.sync.create_sync(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `request`                                            | [shared.SyncInput](../../models/shared/syncinput.md) | :heavy_check_mark:                                   | The request object to use for the request.           |


### Response

**[operations.CreateSyncResponse](../../models/operations/createsyncresponse.md)**


## get_syncs

Get all syncs

### Example Usage

```python
import fabra

s = fabra.Fabra(
    api_key_auth="",
)


res = s.sync.get_syncs()

if res.object is not None:
    # handle response
    pass
```


### Response

**[operations.GetSyncsResponse](../../models/operations/getsyncsresponse.md)**

