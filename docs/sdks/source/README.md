# source

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
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.SourceInput(
    bigquery_config=shared.BigQueryConfig(
        credentials='Paste JSON from GCP',
        location='us-west1',
    ),
    connection_type=shared.ConnectionType.SNOWFLAKE,
    display_name='Frontend Events',
    end_customer_id='abcd-1234-efgh-5678',
    mongodb_config=shared.MongoDbConfig(
        connection_options='retryWrites=true&w=majority',
        host='examplecluster.abc123.mongodb.net',
        password='securePassword123',
        username='jane_doe',
    ),
    redshift_config=shared.RedshiftConfig(
        database_name='your_database',
        host='examplecluster.12345.us-west-1.redshift.amazonaws.com',
        password='securePassword123',
        port='5432',
        username='jane_doe',
    ),
    snowflake_config=shared.SnowflakeConfig(
        database_name='your_database',
        host='abc123.us-east4.gcp.snowflakecomputing.com',
        password='securePassword123',
        role='your_role',
        username='jane_doe',
        warehouse_name='your_warehouse',
    ),
)

res = s.source.create_source(req)

if res.create_source_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `request`                                                | [shared.SourceInput](../../models/shared/sourceinput.md) | :heavy_check_mark:                                       | The request object to use for the request.               |


### Response

**[operations.CreateSourceResponse](../../models/operations/createsourceresponse.md)**


## get_sources

Get all sources

### Example Usage

```python
import fabra


s = fabra.Fabra(
    security=shared.Security(
        api_key_auth="",
    ),
)


res = s.source.get_sources()

if res.get_sources_200_application_json_object is not None:
    # handle response
```


### Response

**[operations.GetSourcesResponse](../../models/operations/getsourcesresponse.md)**

