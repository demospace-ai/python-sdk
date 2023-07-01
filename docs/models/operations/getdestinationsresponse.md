# GetDestinationsResponse


## Fields

| Field                                                                                                       | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                              | *str*                                                                                                       | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `status_code`                                                                                               | *int*                                                                                                       | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `raw_response`                                                                                              | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                       | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `get_destinations_200_application_json_object`                                                              | [Optional[GetDestinations200ApplicationJSON]](../../models/operations/getdestinations200applicationjson.md) | :heavy_minus_sign:                                                                                          | Successfully fetched destinations                                                                           |