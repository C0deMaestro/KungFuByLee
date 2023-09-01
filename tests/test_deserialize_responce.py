import pytest
from view import *

@pytest.mark.parametrize("json_input,http_dct",
                         [('{"key": "value"}', {'key': 'value'}),
                          ('{"name": "John"}', {'name': 'John'}),
                          ('{"numbers": [1, 2, 3]}', {'numbers': [1, 2, 3]}),
                          ])
def test_deseriallize_succes(json_input,http_dct):
    expected = (
        "HTTP/1.1 200 OK\r\n"
        f"Content-Length: {len(http_dct)}\r\n"
        "Content-Type: application/json\r\n"
        "\r\n"
        f"{http_dct}"
    )
    assert deserialize(json_input) == expected


def test_deseriallize_fail():
    json_input = '{}'
    expected = (
        "HTTP/1.1 200 OK\r\n"
        f"Content-Length: {1}\r\n"
        "Content-Type: application/json\r\n"
        "\r\n"
        '{"key": "value"}'
    )
    assert deserialize(json_input) != expected