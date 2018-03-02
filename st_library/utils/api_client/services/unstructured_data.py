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

"""Implements BigQuery HTTP API wrapper."""

import sys

from st_library.utils.api_client import http, endpoints


class UnstructuredDataService(object):
    """A helper class to issue BigQuery HTTP requests."""

    def __init__(self):
        """Initializes the BigQuery helper with context information.

        """

    def tables_get(self, table_name, matrices_id):
        """Issues a request to retrieve information about a table.

        Args:
          table_name: a tuple representing the full name of the table.
        Returns:
          A parsed result object.
        Raises:
          Exception if there is an error performing the operation.
        """
        url = endpoints.object_path(table_name, matrices_id)
        return http.Http.request(url)

    def download_object(self, datasetsid, file_name):
        """ Download an object.

        Args:
          datasetsid: the id of the dataset.
          file_name: the name of the dataset files.
        Returns:
          A url for downloading object.
        Raises:
          Exception if there is an error performing the operation.
        """
        url = endpoints.object_download_path(datasetsid, file_name)
        download_url = http.Http.request(url, raw_response=True)
        return http.Http.request(download_url, raw_response=True)

    def upload_object(self, datasetsid, file_name, file_path):
        """ Upload file to gcs.

        Args:
          file_name: the name of the file.
          file_path: the path of the file.
        Returns:
          A result object.
        Raises:
          Exception if there is an error performing the operation.
        """

        url = endpoints.object_path(datasetsid, file_name)

        if sys.version > '3':
            from requests_toolbelt.multipart.encoder import MultipartEncoder

            multipart_data = MultipartEncoder(
                fields={
                    # a file upload field
                    'file': (file_name,
                             open(file_path + file_name,
                                  'rb'), 'text/plain')
                }
            )
            headers = {}
            headers['Content-Type'] = multipart_data.content_type

            return http.Http.request(url=url, data=multipart_data, headers=headers, method='POST')
        else:
            from poster.encode import multipart_encode
            from poster.streaminghttp import register_openers

            # Register the streaming http handlers with urllib2
            register_openers()

            # Start the multipart/form-data encoding of the file
            # "file" is the name of the parameter, which is normally set
            # via the "name" parameter of the HTML <input> tag.
            # headers contains the necessary Content-Type and Content-Length
            # datagen is a generator object that yields the encoded parameters
            datagen, headers = multipart_encode(
                {"file": open(file_path + file_name)})
            return http.Http.request(url=url, data=datagen, headers=headers, method='POST')

    def delete_object(self, datasetsid, file_name):
        """ Delete an object.

        Args:
          datasetsid: the id of the dataset.
          file_name: the name of the dataset files.
        Returns:
          A url for downloading object.
        Raises:
          Exception if there is an error performing the operation.
        """
        url = endpoints.object_path(datasetsid, file_name)
        return http.Http.request(url=url, method='DELETE')
