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
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.QueryObjectRequest(
    request_body=operations.QueryObjectRequestBody(
        filters=[
            shared.QueryFilter(
                field_name='user_id',
                field_value='2',
            ),
        ],
    ),
    end_customer_id='vel',
    object_id=623564,
)

res = s.customer_data.query_object(req)

if res.query_object_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.QueryObjectRequest](../../models/operations/queryobjectrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.QueryObjectResponse](../../models/operations/queryobjectresponse.md)**

