<!-- Start SDK Example Usage -->
```python
import fabra
from fabra.models import operations

s = fabra.Fabra(
    security=shared.Security(
        api_key_auth="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetNamespacesRequest(
    connection_id=548814,
)

res = s.connection.get_namespaces(req)

if res.namespaces is not None:
    # handle response
```
<!-- End SDK Example Usage -->