import functools
import requests
import suds.transport as transport
import traceback

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

        return transport.Reply(
            resp.status_code,
            resp.headers,
            resp.content,
        )
