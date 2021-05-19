from htminify import minify


class StripWhitespaceMiddleware(object):
    """wsgi middleware that strips extra whitespace from html"""

    def __init__(self, app, encoding="utf-8"):
        self.app = app
        self.encoding = encoding

    def __call__(self, environ, start_response):
        app_iter = self.app(environ, start_response)
        html = b"".join(app_iter).decode(self.encoding)
        return [minify(html).encode(self.encoding)]
