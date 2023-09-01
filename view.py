from class_router import Router
import json

app = Router()


def deserialize(response_dct):
    response_dct = json.dumps(response_dct)
    http_response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Length: {}\r\n"
        "Content-Type: application/json\r\n"
        "\r\n"
        "{}"
    ).format(len(response_dct), response_dct)

    return http_response


@app.route_dec("/api/v1/books/")
def books_home():
    dct = {1:"tolstoy",2:"dostoevski"}
    return dct


@app.route_dec(r"/api/v1/books/\d+/")
def books_item():
    dct = {123: "kniga_123", 345: "kniga_345"}
    return dct


@app.route_dec(r"/api/v1/books/\d+/authors/")
def books_authors():
    dct = {"kniga_345": "author is sesenin"}
    return dct


@app.route_dec("/api/v1/categories/")
def categories():
    dct = {1: "tolstushki", 2: "anal", 3:"brother and mom and sister"}
    return dct


@app.route_dec(r"/api/v1/books/\d+/categories/")
def books_categories():
    dct = {"kniga po nomeru": "category"}
    return dct
