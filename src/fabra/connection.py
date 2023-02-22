import requests
from . import utils
from fabra.models import operations
from typing import Optional

class Connection:
    _client: requests.Session
    _security_client: requests.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests.Session, security_client: requests.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version

    
    def get_namespaces(self, request: operations.GetNamespacesRequest) -> operations.GetNamespacesResponse:
        r"""Get all namespaces
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/connection/namespaces"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetNamespacesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetNamespaces200ApplicationJSON])
                res.get_namespaces_200_application_json_object = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 500:
            pass

        return res

    
    def get_schema(self, request: operations.GetSchemaRequest) -> operations.GetSchemaResponse:
        r"""Get schema for table
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/connection/schema"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetSchemaResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetSchema200ApplicationJSON])
                res.get_schema_200_application_json_object = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 500:
            pass

        return res

    
    def get_tables(self, request: operations.GetTablesRequest) -> operations.GetTablesResponse:
        r"""Get all tables
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/connection/tables"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetTablesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetTables200ApplicationJSON])
                res.get_tables_200_application_json_object = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 500:
            pass

        return res

    