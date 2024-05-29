# LinkToken
(*link_token*)

## Overview

Operations on link tokens

### Available Operations

* [create_link_token](#create_link_token) - Create a new link token

## create_link_token

Create a new link token

### Example Usage

```python
import fabra
from fabra.models import components

s = fabra.Fabra(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.link_token.create_link_token(request=components.CreateLinkTokenRequest(
    end_customer_id='abcd-1234-efgh-5678',
))

if res.create_link_token_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.CreateLinkTokenRequest](../../models/components/createlinktokenrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateLinkTokenResponse](../../models/operations/createlinktokenresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
