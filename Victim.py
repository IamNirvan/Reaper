import platform


class Victim:
    def __init__(self):
        self.system = platform.system()
        self.processor = platform.processor()
        self.machine = platform.machine()

    def __str__(self):
        print(f"System: {self.system}")
        print(f"Processor: {self.processor}")
        print(f"Machine: {self.machine}")

    def get_system(self):
        return self.system;

    def get_processor(self):
        return self.processor;

    def get_machine(self):
        return self.machine;
