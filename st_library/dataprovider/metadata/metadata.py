from collections import defaultdict

from st_library.dataprovider.metadata.script_execution_configuration import ScriptExecutionConfiguration
from st_library.dataprovider.utils.helpers.store import Store


class Metadata(object):
    def __init__(self):
        self._script_execution_configurations = defaultdict(ScriptExecutionConfiguration)

    def get_parameter_value(self, parameter_id):
        return self._script_execution_configurations[Store.configuration_uuid].get_parameter_value(parameter_id)
