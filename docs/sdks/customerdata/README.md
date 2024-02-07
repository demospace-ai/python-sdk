# CustomerData
(*customer_data*)

### Available Operations

* [query_object](#query_object) - Query object record for customer

## query_object

Query a single object record directly from a customer's source. The response payload will match the object schema you've defined.

### Example Usage

```python
import fabra
from fabra.models import operations, shared

s = fabra.Fabra(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.QueryObjectRequest(
    end_customer_id='string',
    object_id=906396,
    request_body=operations.QueryObjectRequestBody(
        filters=[
            shared.QueryFilter(
                field_name='user_id',
                field_value='2',
            ),
        ],
    ),
)

res = s.customer_data.query_object(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.QueryObjectRequest](../../models/operations/queryobjectrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.QueryObjectResponse](../../models/operations/queryobjectresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
