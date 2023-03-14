import socket
from Reaper import Reaper

SERVER_IP = "192.168.1.176"
SERVER_PORT = 4678

class Reaper_client(Reaper):

    def connect(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((SERVER_IP, SERVER_PORT))
            data = sock.recv(1024)
            print(f"Received: {data}")

        input("Press any key to exit...")



if __name__ == '__main__':
    client = Reaper_client()
    client.connect()
