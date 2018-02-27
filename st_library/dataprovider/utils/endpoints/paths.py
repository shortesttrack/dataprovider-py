from urlobject import URLObject


ROOT = URLObject('https://shortesttrack.com')

METADATA_ENDPOINT = ROOT.add_path('api/metadata/')


def sec_get_detail_path(uuid):
    return METADATA_ENDPOINT.add_path('script-execution-configurations/{uuid}'.format(uuid=uuid))
