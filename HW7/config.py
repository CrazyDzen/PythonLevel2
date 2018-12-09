from socket import socket, AF_INET, SOCK_STREAM
from jim_protocol import get_presence, get_response
import json
import time


ADDRESS = "localhost"
PORT = 7777


def send_presence(s):
    s.send(json.dumps(get_presence()).encode("utf-8"))
    resp = json.loads(s.recv(1024).decode("utf-8"))
    return resp


def get_client():
    s = socket()
    try:
        s.connect((ADDRESS, PORT))
    except ConnectionRefusedError:
        return get_response(500), s
    resp = send_presence(s)
    return resp, s


def get_server():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((ADDRESS, PORT))
    s.listen(5)
    s.settimeout(0.2)
    return s
