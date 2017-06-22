# -*- coding: utf-8 -*-
"""Swagger generated client 'monkey-patch' for logging API requests

isort:skip_file
"""

from config import ORCID_API_BASE
from flask_login import current_user
from models import OrcidApiCall
from swagger_client import configuration, rest
from urllib.parse import urlparse

url = urlparse(ORCID_API_BASE)
configuration.host = url.scheme + "://" + url.hostname


class HubRESTClientObject(rest.RESTClientObject):
    def request(self,
                method,
                url,
                query_params=None,
                headers=None,
                body=None,
                post_params=None,
                _preload_content=True,
                _request_timeout=None,
                **kwargs):

        put_code = body.get("put-code") if body else None
        try:
            OrcidApiCall.create(
                user_id=current_user.id,
                method=method,
                url=url,
                query_params=query_params,
                body=body,
                put_code=put_code)
        except Exception as ex:
            # TODO: log the failure
            pass
        return super().request(
            method=method,
            url=url,
            query_params=query_params,
            headers=headers,
            body=body,
            post_params=post_params,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            **kwargs)


# yapf: disable
from swagger_client import *  # noqa: F401, F403, F405
api_client.RESTClientObject = HubRESTClientObject  # noqa: F405
apis.member_apiv20_api.ApiClient = HubApiClient  # noqa: F405
