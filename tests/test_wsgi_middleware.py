from htminify import wsgi
from helpers import WsgiApp
from unittest.mock import Mock

def test_functionality():
    app = WsgiApp(Mock, Mock)
    app_with_middleware = wsgi.StripWhitespaceMiddleware(app)
    middleware_response = app_with_middleware.__call__(Mock(), Mock())

    assert app.original_html != middleware_response
    assert app.minified_html == middleware_response
