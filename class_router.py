from functools import wraps
import re


class Router:
    def __init__(self):
        self.urls = []

    def route_dec(self, path):
        def func_dec(func):
            self.urls.append((path, func))

            @wraps(func)
            def inner(*args, **kwargs):
                return func(*args, **kwargs)

            return inner

        return func_dec

    def router_url(self, request):
        path = request.get("path")
        for url in self.urls:
            if re.fullmatch(url[0], path):
                return url[1]()
