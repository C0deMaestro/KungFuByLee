from class_router import Router
import json

app = Router()


def deserialize(responce):
    response_dct = json.loads(responce)
    # response_dct = responce
    http_response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Length: {}\r\n"
        "Content-Type: application/json\r\n"
        "\r\n"
        "{}"
    ).format(len(response_dct), response_dct)
    return http_response


@app.route_dec("/api/v1/books/")
def books_home(request):
    print("books_home")


@app.route_dec(r"/api/v1/books/\d+/")
def books_item(request):
    print("books_item")


@app.route_dec(r"/api/v1/books/\d+/authors/")
def books_authors(request):
    print("books_authors")


@app.route_dec("/api/v1/categories/")
def categories(request):
    print("categories")


@app.route_dec(r"/api/v1/books/\d+/categories/")
def books_categories(request):
    print("books_categories")
