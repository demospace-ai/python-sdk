import requests
from . import utils
from fabra.models import operations
from typing import Optional

class Object:
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

    
    def create_object(self, request: operations.CreateObjectRequest) -> operations.CreateObjectResponse:
        r"""Create a new object
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/object"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._security_client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateObjectResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.CreateObject200ApplicationJSON])
                res.create_object_200_application_json_object = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 500:
            pass

        return res

    
    def get_objects(self) -> operations.GetObjectsResponse:
        r"""Get all objects
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/objects"
        
        
        client = self._security_client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetObjectsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetObjects200ApplicationJSON])
                res.get_objects_200_application_json_object = out
        elif r.status_code == 401:
            pass
        elif r.status_code == 500:
            pass

        return res

    