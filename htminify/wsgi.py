from htminify import minify

class StripWhitespaceMiddleware(object):
    """wsgi middleware that strips extra whitespace from html"""

    def __init__(self, app, encoding="utf-8"):
        self.app = app
        self.encoding = encoding

    def __call__(self, environ, start_response):
        inner_status = None
        inner_headers = []
        inner_exc_info = None

        def start_response_collector(status, headers, exc_info=None):
            # Just collects the inner response headers, to be modified before sending to client
            nonlocal inner_status, inner_headers, inner_exc_info
            inner_status = status
            inner_headers = headers
            inner_exc_info = exc_info
            # Not calling start_response(), as we will modify the headers first.
            return None

        # populates the inner_* vars, as triggers inner call of the collector closure
        response_iter = self.app(environ, start_response_collector)

        # removes the content-length, if exists
        headers = [(k, v) for k, v in inner_headers if k.lower() != 'content-length']

        html = b"".join(response_iter)
        html = html.decode("utf-8")


        ### MANIPULATE YOUR `inner_body` HERE ###
        # E.g. producing a final_body
        final_body = minify(html)

        headers.append(('Content-Length', str(len(final_body))))

        # Remember to send the modified headers!
        start_response(inner_status, headers, inner_exc_info)   
        return [final_body.encode("utf-8")]
