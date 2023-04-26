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
        api_key_auth="YOUR_API_KEY_HERE",
    ),
)


req = shared.CreateLinkTokenRequest(
    end_customer_id="123",
)

res = s.link_token.create_link_token(req)

if res.create_link_token_response is not None:
    # handle response
```
