from view import *
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("/api/v1/books/", books_home),
        ("/api/v1/books/1337/", books_item),
        ("/api/v1/books/1337/authors/",books_authors),
        ("/api/v1/categories/", categories),
        ("/api/v1/books/1337/categories/",books_categories),
    ],
)
def test_router_url__success(test_input, expected):
    assert app.router_url({"path":test_input}).__name__ == expected.__name__

def test_router_url__fail():
    assert app.router_url({"path": "/api/v1/books/"}).__name__ != books_item.__name__
