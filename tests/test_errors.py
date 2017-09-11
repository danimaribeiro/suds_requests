import pytest
import requests
import suds.transport

from unittest import mock
from suds_requests import handle_errors


def test_no_errors():
    m = mock.Mock(__name__='m')
    f = handle_errors(m)
    assert f() == m.return_value


def test_HTTPError():
    resp = mock.Mock(status_code=404)
    m = mock.Mock(
        side_effect=requests.HTTPError(response=resp),
        __name__='m',
    )
    f = handle_errors(m)
    with pytest.raises(suds.transport.TransportError) as excinfo:
        f()
    assert excinfo.value.httpcode == 404


def test_RequestException():
    m = mock.Mock(
        side_effect=requests.RequestException(),
        __name__='m',
    )
    f = handle_errors(m)
    with pytest.raises(suds.transport.TransportError) as excinfo:
        f()
    assert excinfo.value.httpcode == 000
