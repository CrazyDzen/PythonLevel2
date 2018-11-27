import socket
from jim_protocol import get_presence, get_response
import json

ADDRESS = "localhost"
PORT = 7777


def get_client():
    s = socket.socket()
    try:
        s.connect((ADDRESS, PORT))
    except ConnectionRefusedError:
        return get_response(500), s
    s.send(json.dumps(get_presence()).encode("utf-8"))
    resp = json.loads(s.recv(1024).decode("utf-8"))
    return resp, s


def get_server():
    s = socket.socket()
    s.bind((ADDRESS, PORT))
    s.listen(3)
    return s
