from client import run_client
import threading
import socket
import unittest
from config import *


class TestPresence(unittest.TestCase):
    def test_server_run(self):
        t = threading.Thread(target=run_client, daemon=True)
        t.start()
        s = socket.socket()
        s.bind((ADDRESS, PORT))
        s.listen(3)
        print("Server started")
        presence = {
            "action": "presence",
            "type": "status",
            "user": {
                "status": "onlain"
            }
        }
        try:
            client, addr = s.accept()
            data = json.loads(client.recv(1024).decode("utf-8"))
            self.assertEqual(data, presence)
            s.close()
        except socket.timeout as err:
            self.fail("Accept failed")


if __name__ == '__main__':
    unittest.main()
