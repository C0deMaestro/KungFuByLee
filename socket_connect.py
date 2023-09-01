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
                data = conn.recv(1024)
                decoding = decode(data)#получаем правильный словарь с данными
                dct = app.router_url(decoding)#вызываем функцию по path который получили, вернем просто словарь в формате json
                response = deserialize(dct)#преобразуем словарь в http ответ и закодируем его в байты
                conn.sendall(response)#отправим
start_server()