from server import run
import threading
import socket
import unittest
from config import *


class TestPresence(unittest.TestCase):
    def test_server_run(self):
        t = threading.Thread(target=run, daemon=True)
        t.start()
        s = socket.socket()
        s.connect((ADDRESS, PORT))
        print("Client connected")
        data = {
            "action": "presence",
        }
        try:
            s.send(json.dumps(data).encode("utf-8"))
            self.assertIsNotNone(s.recv(1024))
            s.close()
        except socket.timeout as err:
            self.fail("Accept failed")





if __name__ == '__main__':
    unittest.main()