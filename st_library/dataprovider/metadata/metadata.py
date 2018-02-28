from collections import defaultdict

from st_library.dataprovider._http import Http
from st_library.dataprovider.models.script_execution_configuration import ScriptExecutionConfiguration
from st_library.dataprovider.utils.endpoints import paths
from st_library.dataprovider.utils.helpers.store import Store


class Metadata(object):
    def __init__(self):
        self._script_execution_configurations = defaultdict(ScriptExecutionConfiguration)

    def get_parameter_value(self, parameter_id):
        return self._script_execution_configurations[Store.configuration_uuid].get_parameter_value(parameter_id)

    def set_performance_output_parameter_value(self, parameter_id, parameter_value):
        if not Store.performance_id:
            raise ValueError('performance_id is not specified in this environment')

        performance_id = Store.performance_id
        Http.request(paths.performance_output_parameter_post_path(parameter_id, performance_id),
                     data={'value': parameter_value}, method='POST')
