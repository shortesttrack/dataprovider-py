from st_library.utils.api_client import endpoints
from st_library.utils.api_client._http import Http
from st_library.utils.generics.base_object import BaseModel
from st_library.utils.helpers.store import Store


class ScriptExecutionConfiguration(BaseModel):
    def get_initial_data(self):
        return Http.request(endpoints.sec_get_detail_path(Store.configuration_uuid), method='GET')

    def get_parameter_value(self, parameter_id):
        for parameter in self['parameters']:
            if parameter['id'] == parameter_id:
                return parameter['value']

        raise ValueError('Parameter does not exist')
