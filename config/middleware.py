import time

class PerformanceMiddleware:
    """
    Intercepts every request and response to measure how long it takes to process.
    Injects an 'X-Response-Time-ms' header into the final HTTP response.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware) are called.
        start_time = time.time()
        
        # The actual view logic runs here
        response = self.get_response(request)
        
        # Code to be executed for each request/response after the view is called.
        duration = time.time() - start_time
        response['X-Response-Time-ms'] = str(int(duration * 1000))
        
        return response
