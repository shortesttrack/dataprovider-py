import os


class Store(object):
    def __init__(self):
        raise TypeError('This class should not be initialized')

    config_id = os.environ.get('CONFIGURATION_ID')

    if os.environ.get('ST_API_TOKEN'):
        token = 'Bearer ' + os.environ['ST_API_TOKEN']
    else:
        token = None

    performance_id = os.environ.get('PERFORMANCE_ID')
