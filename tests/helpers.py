from unittest.mock import MagicMock


class WsgiApp:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response
        # convenience attribut for use in test
        self.original_html = "<html>           </html>".encode("utf-8")
        self.minified_html = ["<html></html>".encode("utf-8")]

    def __iter__(self):
        body = "<html>           </html>".encode("utf-8")
        yield body

    def __call__(self, environ, start_response):
        start_response(MagicMock(), MagicMock())
        return self
