from htminify import minify


class StripWhitespaceMiddleware(object):
    """wsgi middleware that strips extra whitespace from html"""

    def __init__(self, app, encoding="utf-8"):
        self.app = app
        self.encoding = encoding

    def __call__(self, environ, start_response):
        """ Call during request/response cycle"""
        responseInterceptor = ResponseInterceptor(self.app, environ, start_response)
        html = responseInterceptor.get_response_content()
        modified_html = self._modify_response_content(html)

        responseInterceptor.modify_content_headers(modified_html)
        responseInterceptor.send_modified_response_headers()
        return [modified_html]

    def _modify_response_content(self, content):
        """Converts the content to a string using appropriate encoding."""
        content = b"".join(content)
        content = content.decode(self.encoding)
        modified_content = minify(content)
        return modified_content.encode(self.encoding)


# TODO find a better name for class. move to another file?
class ResponseInterceptor:
    """Intercepts the start_response function called by the app. 

    This is necessary to modify the content headers when minifying the Content,
    otherwise The webpage won't render."""

    def __init__(self, app, environ, start_response):
        self.app = app
        self.environ = environ
        self.start_response = start_response

        self.captured_status = None
        self.captured_exc_info = None
        self.captured_headers = []
        self.modified_headers = []

    def get_response_content(self):
        """Returns an iterable app that can be iterated to get the response bytes.

        A closure is necessary because when self.app() is called, It has the side effect
        of calling start_response(status, headers, exc_info)
        So the headers need to be captured so that they can be modified"""
        
        return self.app(self.environ, self._capture_response_values)

    def _capture_response_values(self, status, headers, exc_info=None):
        """A closure that intercepts the headers sent by app."""
        self.captured_status = status
        self.captured_headers = headers
        self.captured_exc_info = exc_info
        return None

    def modify_content_headers(self, modified_content) -> None:
        """ Modifies the content length header since minifying HTML reduces content length."""
        self.modified_headers = [
            (k, v) for k, v in self.captured_headers if k.lower() != "content-length"
        ]
        self.modified_headers.append(("Content-Length", str(len(modified_content))))

    def send_modified_response_headers(self):
        """ Since the start_response() function was not triggered when self.app() was called,
        it has to be manually triggered."""
        self.start_response(
            self.captured_status, self.modified_headers, self.captured_exc_info
        )
