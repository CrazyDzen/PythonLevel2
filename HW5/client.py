from config import get_client
from menu import get_command, print_menu
import json
from log import client_log_config as cl_config

log = cl_config.logger


def send_data(sock):
    
    data = {
        "text": input("Input text: ")
    }
    
    sock.send(json.dumps(data).encode("utf-8"))
    log.info("Message sent")
    print("the message is sent")


def exit_program(sock):
    sock.send(json.dumps({"exit": ""}).encode("utf-8"))
    print("Exit")
    log.info("Client off")
    exit()


def run_client():
    log.info("Client started")
    resp, s = get_client()
    al = str(resp['alert'])
    print(al)
    not_error = [100, 101, 200, 201, 202]
    if resp['response'] not in not_error:
        log.error("%", al)
        print(f"error: {resp['response'], resp['alert']}")
    else:
        log.info("%s", al)
        menu = ["Send data", "Exit"]
        actions = {"1": send_data, "2": exit_program}
        while True:
            print_menu(menu)
            command = get_command(menu)
            actions[command](s)


if __name__ == "__main__":
    run_client()
