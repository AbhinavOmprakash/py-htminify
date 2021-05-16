from htminify import minify

class StripWhitespaceMiddleware(MiddlewareMixin):
    """
    Strips leading and trailing whitespace from response content.
    """
    def process_response(self, request, response):
        response.content = minify(response.content) 
        return response   
        
