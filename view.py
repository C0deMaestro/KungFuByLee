from class_router import Router
import json
import itertools

app = Router()


def deserialize(response_dct, code=200, message= "OK"):
    print(response_dct,code,message)
    http_response = (
        f"HTTP/1.1 {code} {message}\r\n"
        "Content-Length: {}\r\n"
        "Content-Type: application/json\r\n"
        "\r\n"
        "{}"
    ).format(len(response_dct), response_dct)
    print(http_response)
    return http_response.encode()


@app.route_dec("/api/v1/books/")
def books_home(request):
    dct = {1:"tolstoy",2:"dostoevski"}
    return json.dumps(dct)


@app.route_dec(r"/api/v1/books/\d+/")
def books_item(request):
    print(request)
    dct = {request.get("numbers")[0]: "kniga_123", 345: "kniga_345"}
    return json.dumps(dct)


@app.route_dec(r"/api/v1/books/\d+/authors/")
def books_authors(request):
    dct = {request.get("numbers")[0]: "author is sesenin"}
    return json.dumps(dct)


@app.route_dec("/api/v1/categories/")
def categories(request):
    dct = {1: "tolstushki", 2: "anal", 3:"brother and mom and sister"}
    return json.dumps(dct)


@app.route_dec(r"/api/v1/books/\d+/categories/")
def books_categories(request):
    dct = {request.get("numbers")[0]: "category"}
    return json.dumps(dct)

@app.route_dec("404")
def page_not_found(request):
    code = 404
    message = "Page not found"
    dct = {"sorry":"page not found"}
    return json.dumps(dct),code,message


