import functools
import requests
import suds.transport as transport
import traceback
import logging
import sys

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
    from io import BytesIO

__all__ = ['RequestsTransport']


def handle_errors(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except requests.HTTPError as e:
            raise transport.TransportError(
                'Error in requests\n' + traceback.format_exc(),
                e.response.status_code,
            )
        except requests.RequestException:
            raise transport.TransportError(
                'Error in requests\n' + traceback.format_exc(),
                000
            )
    return wrapper


class RequestsTransport(transport.Transport):

    def __init__(self, session=None):
        transport.Transport.__init__(self)
        self._session = session or requests.Session()

        self.log = logging.getLogger('custom_transport')
        self.log.setLevel(logging.DEBUG)
        # self.log.addHandler(logging.StreamHandler(sys.stdout))

    @handle_errors
    def open(self, request):
        resp = self._session.get(request.url)
        return BytesIO(resp.content)

    @handle_errors
    def send(self, request):
        resp = self._session.post(
            request.url,
            data=request.message,
            headers=request.headers,
        )

        self.log.debug('Request HEADERS: {}'.format(request.headers))
        self.log.debug('Request URL: {}'.format(request.url))
        self.log.debug('Request message: {}'.format(request.message))

        print(request.message)

        return transport.Reply(
            resp.status_code,
            resp.headers,
            resp.content,
        )
