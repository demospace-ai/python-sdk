# Fabra Python SDK

<div align="left">
   <p>Use the Fabra API to build customer-facing data warehouse integrations to let your customers start sending data to your application. Unblock your sales pipeline in days, not months.</p>
   <a href="https://github.com/fabra-io/python-sdk/actions"><img src="https://img.shields.io/github/actions/workflow/status/fabra-io/python-sdk/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
   <a href="https://www.fabra.io/#Email-Hero"><img src="https://img.shields.io/static/v1?label=Docs&message=Sign Up&color=2ca47c&style=for-the-badge" /></a>
</div>

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install fabra
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import fabra
from fabra.models import operations

s = fabra.Fabra(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.connection.get_namespaces(request=operations.GetNamespacesRequest(
    connection_id=995455,
))

if res.namespaces is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [connection](docs/sdks/connection/README.md)

* [get_namespaces](docs/sdks/connection/README.md#get_namespaces) - Get all namespaces
* [get_schema](docs/sdks/connection/README.md#get_schema) - Get schema for table
* [get_tables](docs/sdks/connection/README.md#get_tables) - Get all tables

### [customer_data](docs/sdks/customerdata/README.md)

* [query_object](docs/sdks/customerdata/README.md#query_object) - Query object record for customer

### [destination](docs/sdks/destination/README.md)

* [create_destination](docs/sdks/destination/README.md#create_destination) - Create a new destination
* [get_destinations](docs/sdks/destination/README.md#get_destinations) - Get all destinations

### [link_token](docs/sdks/linktoken/README.md)

* [create_link_token](docs/sdks/linktoken/README.md#create_link_token) - Create a new link token

### [object](docs/sdks/object/README.md)

* [create_object](docs/sdks/object/README.md#create_object) - Create a new object
* [get_objects](docs/sdks/object/README.md#get_objects) - Get all objects

### [source](docs/sdks/source/README.md)

* [create_source](docs/sdks/source/README.md#create_source) - Create a new source
* [get_sources](docs/sdks/source/README.md#get_sources) - Get all sources

### [sync](docs/sdks/sync/README.md)

* [create_sync](docs/sdks/sync/README.md#create_sync) - Create a new sync
* [get_syncs](docs/sdks/sync/README.md#get_syncs) - Get all syncs
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

### Example

```python
import fabra
from fabra.models import errors, operations

s = fabra.Fabra(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

res = None
try:
    res = s.connection.get_namespaces(request=operations.GetNamespacesRequest(
    connection_id=995455,
))

except errors.SDKError as e:
    # handle exception
    raise(e)

if res.namespaces is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.fabra.io` | None |

#### Example

```python
import fabra
from fabra.models import operations

s = fabra.Fabra(
    server_idx=0,
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.connection.get_namespaces(request=operations.GetNamespacesRequest(
    connection_id=995455,
))

if res.namespaces is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import fabra
from fabra.models import operations

s = fabra.Fabra(
    server_url="https://api.fabra.io",
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.connection.get_namespaces(request=operations.GetNamespacesRequest(
    connection_id=995455,
))

if res.namespaces is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import fabra
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = fabra.Fabra(client=http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name           | Type           | Scheme         |
| -------------- | -------------- | -------------- |
| `api_key_auth` | apiKey         | API key        |

To authenticate with the API the `api_key_auth` parameter must be set when initializing the SDK client instance. For example:
```python
import fabra
from fabra.models import operations

s = fabra.Fabra(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.connection.get_namespaces(request=operations.GetNamespacesRequest(
    connection_id=995455,
))

if res.namespaces is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
