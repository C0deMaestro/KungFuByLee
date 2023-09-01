from view import *


def test1():
    assert app.router_url({"path": "/api/v1/books/"}).__name__ == books_home.__name__


def test2():
    assert app.router_url({"path": "/api/v1/books/1337/"}).__name__ == books_item.__name__


def test3():
    assert app.router_url({"path": "/api/v1/books/1337/authors/"}).__name__ == books_authors.__name__


def test4():
    assert app.router_url({"path": "/api/v1/categories/"}).__name__ == categoties.__name__


def test5():
    assert app.router_url({"path": "/api/v1/books/1337/categories/"}).__name__ == books_categories.__name__
