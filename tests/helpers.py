from unittest.mock import MagicMock


def construct_django_response():
    # constructs a django response
    html = "<html>           </html>"
    response = MagicMock()
    # django uses utf-8 for encoding
    response.content = html.encode("utf-8")
    return response


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
        return self
