from unittest.mock import MagicMock


class WsgiApp:
    

    def __init__(self, environ, start_response, encoding="utf-8"):
        self.environ = environ
        self.start_response = start_response

        # convenience attributes for use in test
        self.original_html = "<html>           </html>".encode(encoding)
        self.minified_html = ["<html></html>".encode(encoding)]

      def __iter__(self):
        body = self.original_html
        yield body

    def __call__(self, environ, start_response):
        start_response(MagicMock(), MagicMock())
        return self
