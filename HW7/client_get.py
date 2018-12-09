from config import get_client
from menu import get_command, print_menu
import json


def run_client():
    resp, s = get_client()
    al = str(resp['alert'])
    print(al)
    not_error = [100, 101, 200, 201, 202]
    if resp['response'] not in not_error:
        print(f"error: {resp['response'], resp['alert']}")
    else:
        while True:
            print("Waiting data")
            data = json.loads(s.recv(1024).decode("utf-8"))
            if "exit" not in data:
                print(data)
            else:
                print("Exit")
                exit()


if __name__ == "__main__":
    run_client()
