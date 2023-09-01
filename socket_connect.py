import socket
from decode_http import decode
from view import *

def start_server(host='', port=8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(10)
        while True:
            conn, addr = s.accept()
            # start new thread??
            with conn:
                print('Connected by', addr)
                data = conn.recv(1024)
                decoding = decode(data)
                dct= app.router_url(decoding)
                print(dct)
                response = deserialize(dct)
                conn.sendall(response.encode())
start_server()