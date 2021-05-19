"""wsgi middleware """
from htminify import minify

class StripWhitespaceMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        app_iter = self.app(environ, start_response)
        html = b"".join(app_iter).decode("utf8")
        return [minify(html).encode("utf8")]