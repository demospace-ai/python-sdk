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
from fabra.models import components

s = fabra.Fabra(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.source.create_source(request=components.SourceInput(
    connection_type=components.ConnectionType.WEBHOOK,
    display_name='Frontend Events',
    end_customer_id='abcd-1234-efgh-5678',
    bigquery_config=components.BigQueryConfig(
        location='us-west1',
        credentials='Paste JSON from GCP',
    ),
    mongodb_config=components.MongoDbConfig(
        host='examplecluster.abc123.mongodb.net',
        password='securePassword123',
        username='jane_doe',
        connection_options='retryWrites=true&w=majority',
    ),
    redshift_config=components.RedshiftConfig(
        database_name='your_database',
        host='examplecluster.12345.us-west-1.redshift.amazonaws.com',
        password='securePassword123',
        port='5432',
        username='jane_doe',
    ),
    snowflake_config=components.SnowflakeConfig(
        database_name='your_database',
        host='abc123.us-east4.gcp.snowflakecomputing.com',
        password='securePassword123',
        role='your_role',
        username='jane_doe',
        warehouse_name='your_warehouse',
    ),
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [components.SourceInput](../../models/components/sourceinput.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.CreateSourceResponse](../../models/operations/createsourceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

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
| errors.SDKError | 4xx-5xx         | */*             |
