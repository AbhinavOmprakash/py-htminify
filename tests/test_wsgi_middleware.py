from htminify import wsgi
from helpers import WsgiApp
from unittest.mock import Mock

# TODO Improve test suite. Currently does not test ResponseInterceptor properly.


def test_wsgi_middleware_with_default_encoding():
    app = WsgiApp(Mock, Mock, "utf-8")
    app_with_middleware = wsgi.StripWhitespaceMiddleware(app)
    middleware_response = app_with_middleware.__call__(Mock(), Mock())

    assert app.original_html != middleware_response
    assert app.minified_html == middleware_response

def test_wsgi_middleware_with_UTF16_encoding():
    app = WsgiApp(Mock, Mock, "utf-16")

    #Passing another encoding to the middleware
    app_with_middleware = wsgi.StripWhitespaceMiddleware(app, "utf-16") 
    middleware_response = app_with_middleware.__call__(Mock(), Mock())

    assert app.original_html != middleware_response
    assert app.minified_html == middleware_response
