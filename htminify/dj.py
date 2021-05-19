"""Django related functionality"""

from htminify import minify
from django.conf import settings


class StripWhitespaceMiddleware(object):
    """
    Middleware class that minifies HTML.
    Usage

    add to django middleware in settings -

    ::code: python

        MIDDLEWARE = [
            #... all your other middleware
            'htminify.middleware.StripWhitespaceMiddleware',
            ]

    Settings

    Default behavior: minify HTML only when debug is false.

    If you want to minify HTML when debug is true, add this to your settings
    ``ALWAYS_MINIFY = True``
    """

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_response(self, request, response):
        """Function called by django when processing a request."""

        if self._should_minify():
            return self._minify(response)
        else:
            return response

    def _should_minify(self) -> bool:
        """
        Function to Decide whether to minify or not.
        The default behavior is to minify ONLY in production.
        the flag ``ALWAYS_MINIFY`` is used to override the default behaviour.
        """
        try:
            # ALWAYS_MINIFY won't exist if it isn't explicitly set.
            if settings.ALWAYS_MINIFY:
                return True
            else:
                return not settings.DEBUG

        except AttributeError:
            return not settings.DEBUG

    def _minify(self, response):
        """
        Function that's responsible for converting An HTTP response's content
        To a compatible input format i.e string. for minification.
        And converting the output back to a compatible format.
        """
        # Django uses byte strings, and a default encoding of UTF-8.
        # It is unlikely that django will use any other encoding
        # refer to https://docs.djangoproject.com/en/3.2/ref/unicode/
        html = response.content.decode("utf-8")
        response.content = minify(html).encode("utf-8")
        print("calling minify")
        return response
