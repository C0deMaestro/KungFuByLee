from view import *
import re


def router(request):
    path = request.get("path")
    urls = [
        (r"/api/v1/books/", books_home),
        (r"/api/v1/books/\d+/", books_item),
        (r"/api/v1/books/\d+/authors/", books_authors),
        (r"/api/v1/categories/", categoties),
        (r"/api/v1/books/\d+/categories/", books_categories),
    ]
    for url in urls:
        if re.fullmatch(url[0], path):
            url[1](request)
