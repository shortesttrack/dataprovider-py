from collections import defaultdict

from st_library.utils.api_client import ApiClient
from st_library.utils.api_client.models import ScriptExecutionConfiguration
from st_library.utils.helpers.store import Store


class Metadata(object):
    def __init__(self):
        self._script_execution_configurations = defaultdict(ScriptExecutionConfiguration)

    def get_parameter_value(self, parameter_id):
        return self._script_execution_configurations[Store.config_id].get_parameter_value(parameter_id)

    def set_performance_output_parameter_value(self, parameter_id, parameter_value):
        if not Store.performance_id:
            raise ValueError('performance_id is not specified in this environment')

        performance_id = Store.performance_id
        ApiClient.post(ApiClient.res.performance_output_parameter_post(parameter_id, performance_id),
                       data={'value': parameter_value})