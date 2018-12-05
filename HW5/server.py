from config import get_server
from jim_protocol import create_response
import json
from log import server_log_config as ser_config


def run():
    log = ser_config.logger
    s = get_server()
    log.info("Server started")
    print("Server started")
    client, addr = s.accept()
    #print("Client connected: ", client, addr)
    presence = json.loads(client.recv(1024).decode("utf-8"))
    log.info("Presence received ")
    client.send(json.dumps(create_response(presence)).encode("utf-8"))
    log.info("Response sent")

    while True:
        print("Waiting data")
        data = json.loads(client.recv(1024).decode("utf-8"))
        log.info("Data received")
        if "exit" not in data:
            print(data)
        else:
            client.close()
            s.close()
            log.info("Server off")
            print("Exit")
            break


if __name__ == "__main__":
    run()
