import platform
import subprocess


class Victim:
    def __init__(self):
        self.system = platform.system()
        self.processor = platform.processor()
        self.machine = platform.machine()
        self.username = self.get_username()
        self.processor_count = self.get_processor_count()

    def __str__(self):
        print(f"System: {self.system}")
        print(f"Processor: {self.processor}")
        print(f"Machine: {self.machine}")

    def get_username(self):
        if self.system == "Linux":
            name = subprocess.run(["whoami"], capture_output=True, shell=True).stdout.decode("UTF-8").split("\n")[0]
            return name
        elif self.system == "Windows":
            name = subprocess.run(["echo", "%username%"], capture_output=True, shell=True).stdout.decode("UTF-8")\
                .split("\n")[0].split("\r")[0]
            return name

    def get_target_dir(self):
        if self.system == "Linux":
            return rf"/home/{self.username}/Documents"
        elif self.system == "Windows":
            return rf"C:\Users\{self.username}\Documents"

    def get_processor_count(self):
        if self.system == "Linux":
            return "Unkown"
        elif self.system == "Windows":
            return subprocess.run(["echo", "%NUMBER_OF_PROCESSORS%"], capture_output=True, shell=True).stdout.decode("UTF-8") \
                .split("\n")[0].split("\r")[0]
