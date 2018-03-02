from st_library.core.dataprovider.unstructured_data.item import Item


class UnstructuredData(object):
    def __init__(self):
        self.Item = Item

    def download_file(self, datasetsid, filename):
        """
        Download files to disk.
        :return local file path:
        """
        item = self.Item(datasetsid=datasetsid)
        return item.download_file(filename)

    def upload_file(self, datasetsid, filename, filepath):
        """
        Download dataset files to disk.
        :return local file path:
        """
        item = self.Item(datasetsid=datasetsid)
        return item.upload_file(filename, filepath)

    def delete_file(self, datasetsid, filename):
        """
        Download files to disk.
        :return local file path:
        """
        item = self.Item(datasetsid=datasetsid)
        return item.delete_file(filename)
