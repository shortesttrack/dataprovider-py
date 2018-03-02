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
from st_library.core.dataprovider import Item
from st_library.core.dataprovider import Table
from st_library.core.dataprovider.dataprovider import DataProvider
from st_library.core.logger.logger import Logger
from st_library.core.metadata.metadata import Metadata
from st_library.utils.generics.singleton import Singleton
from st_library.utils.helpers.store import Store


__all__ = ('Library',)


class Library(Singleton):
    """
    The Singleton object, which retrieves and holds the Config ID of the Notebook.
    """

    def __init__(self):
        self.metadata = Metadata()
        self.logger = Logger()
        self.data_provider = DataProvider()

    @property
    def config_id(self):
        """
        Retrieves the Configuration UUID.
        :return:
        """

        return Store.config_id

    def set_config_id(self, config_id):
        Store.config_id = config_id

    @property
    def token(self):
        """
        Retrieves the token.
        :return:
        """

        return Store.token

    def set_token(self, token):
        Store.token = token

    @property
    def performance_id(self):
        """
        Retrieves the performance.
        :return:
        """
        return Store.performance_id

    def read_matrix(self, matricesid, datasetsid, tablename):
        """
        Retrieves the table data.
        :return dataframe:
        """
        tbl = Table(matricesid, datasetsid, tablename)
        return (tbl.to_dataframe())

    def read_sec_matrix(self, matricesid, datasetsid, tablename):
        """
        Retrieves the table data.
        :return dataframe:
        """
        tbl = Table(matricesid, datasetsid, tablename, config_related=True)
        return (tbl.to_dataframe())

    def get_parameter(self):
        """
        Retrieves the table data.
        :return dataframe:
        """
        tbl = Table()
        return tbl.get_parameter_data()

    def download_file(self, datasetsid, filename):
        """
        Download files to disk.
        :return local file path:
        """
        item = Item(datasetsid=datasetsid)
        return item.download_file(filename)

    def upload_file(self, datasetsid, filename, filepath):
        """
        Download dataset files to disk.
        :return local file path:
        """
        item = Item(datasetsid=datasetsid)
        return item.upload_file(filename, filepath)

    def delete_file(self, datasetsid, filename):
        """
        Download files to disk.
        :return local file path:
        """
        item = Item(datasetsid=datasetsid)
        return item.delete_file(filename)
