import threading

# Create a thread-local storage object
thread_local = threading.local()

class CustomUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Store the user information in the thread-local storage
        thread_local.user = request.user
        return self.get_response(request)