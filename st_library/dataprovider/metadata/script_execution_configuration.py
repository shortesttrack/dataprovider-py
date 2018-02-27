from st_library.dataprovider.utils.helpers.store import Store
from st_library.dataprovider.utils.generics.base_object import BaseObject
from st_library.dataprovider._http import Http
from st_library.dataprovider.utils.endpoints import paths


class ScriptExecutionConfiguration(BaseObject):
    def get_initial_data(self):
        return Http.request(paths.sec_get_detail_path(Store.configuration_uuid), method='GET')

    def get_parameter_value(self, parameter_id):
        for parameter in self['parameters']:
            if parameter['id'] == parameter_id:
                return parameter['value']

        raise ValueError('Parameter does not exist')
