from htminify import wsgi
from helpers import WsgiApp
from unittest.mock import Mock

#TODO Improve test suite. Currently does not test ResponseInterceptor properly. 
#TODO Add tests for different encoding

def test_wsgi_middleware():
    app = WsgiApp(Mock, Mock)
    app_with_middleware = wsgi.StripWhitespaceMiddleware(app)
    middleware_response = app_with_middleware.__call__(Mock(), Mock())

    assert app.original_html != middleware_response
    assert app.minified_html == middleware_response
