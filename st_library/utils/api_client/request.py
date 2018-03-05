# Copyright 2017 Shortest Track Company. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.

"""Implements HTTP client helper functionality."""
import datetime

import requests

from st_library import exceptions
from st_library.utils.helpers.store import Store


METHOD_GET = 'get'
METHOD_POST = 'post'
METHOD_DELETE = 'delete'


def _request(url, method, params, data, extra_headers,
             raw_response, stats):
    """Issues HTTP requests.

    Args:
      url: the URL to request.
      params: optional query string arguments.
      data: optional data to be sent within the request.
      extra_headers: optional headers to include in the request.
      method: optional HTTP method to use. If unspecified this is inferred
          (GET or POST) based on the existence of request data.
      raw_response: whether the raw response content should be returned as-is.
      stats: an optional dictionary that, if provided, will be populated with some
          useful info about the request, like 'duration' in seconds and 'data_size' in
          bytes. These may be useful optimizing the access to rate-limited APIs.
    Returns:
      The parsed response object.
    Raises:
      Exception when the HTTP request fails or the response cannot be processed.
    """

    headers = dict()
    headers['User-Agent'] = 'st-dataprovider/1.0'
    headers['Authorization'] = Store.token
    headers['Content-Type'] = 'application/json'

    if params:
        # Probably url already has params, just update it
        url.add_query_params(**params)

    if extra_headers:
        headers.update(extra_headers)

    if stats is not None:
        stats['duration'] = datetime.datetime.utcnow()

    response = getattr(requests, method)(url=url, headers=headers, data=data)
    content = response.text
    status_code = response.status_code

    if stats is not None:
        stats['data_size'] = len(data)
        stats['status'] = status_code
        stats['duration'] = (datetime.datetime.utcnow() - stats['duration']).total_seconds()

    if 200 <= status_code < 300:
        if raw_response:
            return content
        return response.json()

    raise exceptions.RequestError(status_code, content)


def get(url, params=None, data=None, extra_headers=None, raw_response=False, stats=None):
    return _request(url, METHOD_GET, params=params, data=data, extra_headers=extra_headers,
                    raw_response=raw_response, stats=stats)


def post(url, params=None, data=None, extra_headers=None, raw_response=False, stats=None):
    if data is None:
        raise exceptions.InvalidRequest('Cannot perform POST request without data')
    return _request(url, METHOD_POST, params=params, data=data, extra_headers=extra_headers,
                    raw_response=raw_response, stats=stats)


def delete(url, params=None, data=None, extra_headers=None, raw_response=False, stats=None):
    return _request(url, METHOD_DELETE, params=params, data=data, extra_headers=extra_headers,
                    raw_response=raw_response, stats=stats)
