from config import get_server
from jim_protocol import create_response
import json


def run():
    s = get_server()
    print("Server started")
    client, addr = s.accept()
    #print("Client connected: ", client, addr)
    presence = json.loads(client.recv(1024).decode("utf-8"))
    client.send(json.dumps(create_response(presence)).encode("utf-8"))

    while True:
        print("Waiting data")
        data = json.loads(client.recv(1024).decode("utf-8"))
        print("Data received")
        if "exit" not in data:
            print(data)
        else:
            client.close()
            s.close()
            print("Exit")
            break


if __name__ == "__main__":
    run()
