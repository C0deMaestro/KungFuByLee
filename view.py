from class_router import Router
import json

app = Router()


def deserialize(response_dct):
    http_response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Length: {}\r\n"
        "Content-Type: application/json\r\n"
        "\r\n"
        "{}"
    ).format(len(response_dct), response_dct)

    return http_response.encode()


@app.route_dec("/api/v1/books/")
def books_home():
    dct = {1:"tolstoy",2:"dostoevski"}
    return json.dumps(dct)


@app.route_dec(r"/api/v1/books/\d+/")
def books_item():
    dct = {123: "kniga_123", 345: "kniga_345"}
    return json.dumps(dct)


@app.route_dec(r"/api/v1/books/\d+/authors/")
def books_authors():
    dct = {"kniga_345": "author is sesenin"}
    return json.dumps(dct)


@app.route_dec("/api/v1/categories/")
def categories():
    dct = {1: "tolstushki", 2: "anal", 3:"brother and mom and sister"}
    return json.dumps(dct)


@app.route_dec(r"/api/v1/books/\d+/categories/")
def books_categories():
    dct = {"kniga po nomeru": "category"}
    return json.dumps(dct)
