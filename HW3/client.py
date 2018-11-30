from config import get_client
from menu import get_command, print_menu
import json


def send_data(sock):
    data = {
        "text": input("Input text: ")
    }

    sock.send(json.dumps(data).encode("utf-8"))

    print("the message is sent")


def exit_program(sock):
    sock.send(json.dumps({"exit": ""}).encode("utf-8"))
    print("Exit")
    exit()


if __name__ == "__main__":
    resp, s = get_client()
    not_error = [100, 101, 200, 201, 202]
    if resp['response'] not in not_error:
        print(f"error: {resp['response'], resp['alert']}")
    else:
        menu = ["Send data", "Exit"]
        actions = {"1": send_data, "2": exit_program}
        while True:
            print_menu(menu)
            command = get_command(menu)
            actions[command](s)
