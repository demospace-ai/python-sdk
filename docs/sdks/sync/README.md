# Sync
(*sync*)

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
from fabra.models import components

s = fabra.Fabra(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.sync.create_sync(request=components.SyncInput(
    destination_id=2,
    display_name='Event Sync',
    end_customer_id='abc123',
    field_mappings=[
        components.FieldMapping(
            destination_field_name='event',
            source_field_name='event_name',
        ),
    ],
    object_id=3,
    source_id=1,
    cursor_field='updated_at',
    custom_join='select * from events join additional_properties on events.id = additional_properties.event_id;',
    frequency=30,
    namespace='end_customer_bigquery_dataset',
    primary_key='event_id',
    table_name='end_customer_events',
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [components.SyncInput](../../models/components/syncinput.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.CreateSyncResponse](../../models/operations/createsyncresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_syncs

Get all syncs

### Example Usage

```python
import fabra

s = fabra.Fabra(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.sync.get_syncs()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetSyncsResponse](../../models/operations/getsyncsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
