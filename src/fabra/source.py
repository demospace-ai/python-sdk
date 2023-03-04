import requests
from . import utils
from fabra.models import operations
from typing import Optional

class Source:
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
        
    def create_source(self, request: operations.CreateSourceRequest) -> operations.CreateSourceResponse:
        r"""Create a new source
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/source'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateSourceResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateSource200ApplicationJSON])
                res.create_source_200_application_json_object = out
        elif http_res.status_code == 401:
            pass
        elif http_res.status_code == 500:
            pass

        return res

    def get_sources(self) -> operations.GetSourcesResponse:
        r"""Get all sources
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/sources'
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetSourcesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetSources200ApplicationJSON])
                res.get_sources_200_application_json_object = out
        elif http_res.status_code == 401:
            pass
        elif http_res.status_code == 500:
            pass

        return res

    