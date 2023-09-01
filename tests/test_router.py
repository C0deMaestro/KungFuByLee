from view import *
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (app.router_url({"path": "/api/v1/books/"}).__name__, books_home.__name__),
        (app.router_url({"path": "/api/v1/books/1337/"}).__name__, books_item.__name__),
        (app.router_url({"path": "/api/v1/books/1337/authors/"}).__name__,books_authors.__name__),
        (app.router_url({"path": "/api/v1/categories/"}).__name__, categories.__name__),
        (app.router_url({"path": "/api/v1/books/1337/categories/"}).__name__,books_categories.__name__),
    ],
)
def test1(test_input, expected):
    assert test_input == expected

def test2_negative():
    assert app.router_url({"path": "/api/v1/books/"}).__name__ != books_item.__name__
