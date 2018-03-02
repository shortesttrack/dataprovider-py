from st_library.core.dataprovider.structured_data.table import Table


class StructuredData(object):
    def __init__(self):
        self.Table = Table

    def read_matrix(self, matricesid, datasetsid, tablename):
        """
        Retrieves the table data.
        :return dataframe:
        """
        tbl = self.Table(matricesid, datasetsid, tablename)
        return (tbl.to_dataframe())

    def read_sec_matrix(self, matricesid, datasetsid, tablename):
        """
        Retrieves the table data.
        :return dataframe:
        """
        tbl = self.Table(matricesid, datasetsid, tablename, config_related=True)
        return (tbl.to_dataframe())

    def get_parameter(self):
        """
        Retrieves the table data.
        :return dataframe:
        """
        tbl = self.Table()
        return tbl.get_parameter_data()
