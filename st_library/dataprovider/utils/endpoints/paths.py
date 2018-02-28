from urlobject import URLObject


ROOT = URLObject('https://shortesttrack.com')

METADATA_ENDPOINT = ROOT.add_path('api/metadata/')
EXECUTION_METADATA_ENDPOINT = ROOT.add_path('api/execution-metadata/')
LOGGING_ENDPOINT = ROOT.add_path('api/logging/')

PERFORMANCES_LIST_GET_PATH = EXECUTION_METADATA_ENDPOINT.add_path('v2/performances/')


def sec_get_detail_path(uuid):
    return METADATA_ENDPOINT.add_path('script-execution-configurations/{uuid}'.format(uuid=uuid))


def performance_get_detail_path(uuid):
    return EXECUTION_METADATA_ENDPOINT.add_path('v2/performances/{uuid}/'.format(uuid=uuid))


def performance_output_parameter_post_path(parameter_id, performance_id):
    return EXECUTION_METADATA_ENDPOINT.\
        add_path('v2/performances/{performance_id}/output-parameters/{parameter_id}/value/'.
                 format(performance_id=performance_id, parameter_id=parameter_id))


def logging_post_path(performance_id):
    return LOGGING_ENDPOINT.add_path('performances/{performance_id}/'.format(performance_id=performance_id))
