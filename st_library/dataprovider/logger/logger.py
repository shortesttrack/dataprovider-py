import six

from st_library.dataprovider._http import Http
from st_library.dataprovider.utils.endpoints import paths
from st_library.dataprovider.utils.helpers.store import Store

MODE_PRINT = 'mode_print'
MODE_SEND = 'mode_send'

LEVEL_DEBUG = 'DEBUG'
LEVEL_INFO = 'INFO'
LEVEL_NOTICE = 'NOTICE'
LEVEL_WARNING = 'WARNING'
LEVEL_ERROR = 'ERROR'
LEVEL_CRITICAL = 'CRITICAL'
LEVEL_ALERT = 'ALERT'
LEVEL_EMERGENCY = 'EMERGENCY'


class Logger(object):
    def __init__(self):
        self._mode = MODE_SEND if Store.performance_id else MODE_PRINT

    def _format_message(self, message, level):
        return '{level}: {message}'.format(level=level, message=message)

    def _log(self, message, analysis, level):
        if self._mode == MODE_SEND:
            payload = {
                'level': level,
                'analysis': analysis,
                'data': message
            }
            Http.request(paths.logging_post_path(Store.performance_id), data=payload, method='POST')
        else:
            six.print_(self._format_message(message, level))

    def debug(self, message, analysis=False):
        self._log(message, analysis, LEVEL_DEBUG)

    def info(self, message, analysis=False):
        self._log(message, analysis, LEVEL_INFO)

    def notice(self, message, analysis=False):
        self._log(message, analysis, LEVEL_NOTICE)

    def warning(self, message, analysis=False):
        self._log(message, analysis, LEVEL_WARNING)

    def error(self, message, analysis=False):
        self._log(message, analysis, LEVEL_ERROR)

    def critical(self, message, analysis=False):
        self._log(message, analysis, LEVEL_CRITICAL)

    def alert(self, message, analysis=False):
        self._log(message, analysis, LEVEL_ALERT)

    def emergency(self, message, analysis=False):
        self._log(message, analysis, LEVEL_EMERGENCY)
