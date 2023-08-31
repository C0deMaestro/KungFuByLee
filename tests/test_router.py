from path_router import router
from view import *


def test1():
    assert router({"path": "/api/v1/books/"}) is books_home


def test2():
    assert router({"path": "/api/v1/books/1337/"}) is books_item


def test3():
    assert router({"path": "/api/v1/books/1337/authors/"}) is books_authors


def test4():
    assert router({"path": "/api/v1/categories/"}) is categoties


def test5():
    assert router({"path": "/api/v1/books/1337/categories/"}) is books_categories
