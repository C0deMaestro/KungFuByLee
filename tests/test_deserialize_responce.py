import json
from view import *


def test1():
    json = '{"key": "value"}'
    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Length: 1\r\n"
        "Content-Type: application/json\r\n"
        "\r\n"
        "{'key': 'value'}"
    )
    assert deserialize(json) == expected


def test2():
    json = '{"name": "John"}'
    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Length: 1\r\n"
        "Content-Type: application/json\r\n"
        "\r\n"
        "{'name': 'John'}"
    )
    assert deserialize(json) == expected


def test3():
    json = '{"numbers": [1, 2, 3]}'
    expected = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Length: 1\r\n"
        "Content-Type: application/json\r\n"
        "\r\n"
        "{'numbers': [1, 2, 3]}"
    )
    assert deserialize(json) == expected
