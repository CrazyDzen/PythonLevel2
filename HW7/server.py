from config import get_server
from jim_protocol import create_response
import json
import select


def run():
    s = get_server()
    print("Server started")
    clients = []

    while True:
        try:
            client, addr = s.accept()
            presence = json.loads(client.recv(1024).decode("utf-8"))
            client.send(json.dumps(create_response(presence)).encode("utf-8"))
            clients.append(client)
        except OSError as e:
            pass
        data = ''
        try:
            r, w, e = select.select(clients, clients, [], 0)
            for el in r:
                data = json.loads(el.recv(1024).decode("utf-8"))
            for el in w:
                if data != '':
                    el.send(json.dumps(data).encode("utf-8"))
        except Exception as e:
            pass


if __name__ == "__main__":
    run()
