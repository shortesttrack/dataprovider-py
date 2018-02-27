import os


class Store(object):
    configuration_uuid = os.environ.get('CONFIGURATION_ID')

    if os.environ.get('ST_API_TOKEN'):
        token = 'Bearer ' + os.environ['ST_API_TOKEN']
    else:
        token = None
