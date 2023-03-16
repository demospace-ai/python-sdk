<!-- Start SDK Example Usage -->
```python
import fabra
from fabra.models import operations, shared

s = fabra.Fabra(
    security=shared.Security(
        api_key_auth=shared.SchemeAPIKeyAuth(
            api_key="YOUR_API_KEY_HERE",
        ),
    ),
)

   
req = operations.GetNamespacesRequest(
    query_params=operations.GetNamespacesQueryParams(
        connection_id=548814,
    ),
)
    
res = s.connection.get_namespaces(req)

if res.get_namespaces_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->