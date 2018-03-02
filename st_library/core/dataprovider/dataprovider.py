from st_library.core.dataprovider.structured_data.structured_data import StructuredData
from st_library.core.dataprovider.unstructured_data.unstructured_data import UnstructuredData


class DataProvider(object):
    def __init__(self):
        self.struct_data = StructuredData()
        self.unstruct_data = UnstructuredData()
