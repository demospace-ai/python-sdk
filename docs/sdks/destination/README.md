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
from fabra.models import components

s = fabra.Fabra(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.destination.create_destination(request=components.DestinationInput(
    connection_type=components.ConnectionType.SNOWFLAKE,
    display_name='BigQuery',
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

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [components.DestinationInput](../../models/components/destinationinput.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.CreateDestinationResponse](../../models/operations/createdestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

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
| errors.SDKError | 4xx-5xx         | */*             |
