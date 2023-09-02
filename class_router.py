from functools import wraps
import re

class Router:
    def __init__(self):
        self.urls = []
        self.page_not_found = None

    def route_dec(self, path):
        def func_dec(func):
            @wraps(func)
            def inner(*args, **kwargs):
                return func(*args, **kwargs)
            if path == "404":
                self.page_not_found = func
                return inner
            self.urls.append((path, func))
            return inner

        return func_dec

    def router_url(self, request):
        path = request.get("path")
        for url in self.urls:
            if re.fullmatch(url[0], path):
                return url[1](request)
        return self.page_not_found(request)
