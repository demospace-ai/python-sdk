<!-- Start SDK Example Usage [usage] -->
```python
import fabra
from fabra.models import operations

s = fabra.Fabra(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetNamespacesRequest(
    connection_id=995455,
)

res = s.connection.get_namespaces(req)

if res.namespaces is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->