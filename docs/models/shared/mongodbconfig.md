# MongoDbConfig


## Fields

| Field                             | Type                              | Required                          | Description                       | Example                           |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `host`                            | *str*                             | :heavy_check_mark:                | N/A                               | examplecluster.abc123.mongodb.net |
| `password`                        | *str*                             | :heavy_check_mark:                | N/A                               | securePassword123                 |
| `username`                        | *str*                             | :heavy_check_mark:                | N/A                               | jane_doe                          |
| `connection_options`              | *Optional[str]*                   | :heavy_minus_sign:                | N/A                               | retryWrites=true&w=majority       |