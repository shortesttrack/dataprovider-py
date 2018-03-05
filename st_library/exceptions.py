import json


class STLibraryException(Exception):
    pass


class RequestError(STLibraryException):
    def __init__(self, status, content):
        self.status = status
        self.content = content
        self.message = u'HTTP request failed. Status code : {} '.format(status)
        # Try extract a message from the body; swallow possible resulting ValueErrors and KeyErrors.
        try:
            error = json.loads(content)['error']
            if 'errors' in error:
                error = error['errors'][0]
            self.message += u': ' + error['message']
        except Exception:
            if content:
                lines = content.split(u'\n')
                if lines:
                    self.message += u': ' + lines[0]

    def __str__(self):
        return self.message


class InvalidRequest(STLibraryException):
    pass
