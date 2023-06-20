# link_token

## Overview

Operations on link tokens

### Available Operations

* [create_link_token](#create_link_token) - Create a new link token

## create_link_token

Create a new link token

### Example Usage

```python
import fabra
from fabra.models import shared

s = fabra.Fabra(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateLinkTokenRequest(
    end_customer_id='abcd-1234-efgh-5678',
)

res = s.link_token.create_link_token(req)

if res.create_link_token_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.CreateLinkTokenRequest](../../models/shared/createlinktokenrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateLinkTokenResponse](../../models/operations/createlinktokenresponse.md)**

