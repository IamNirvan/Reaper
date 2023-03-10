import os
from cryptography.fernet import Fernet


def get_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()


class Saviour:
    targets = []

    def gather_targets(self):
        for file in os.listdir():
            if file == "Reaper.py" or file == "key.key" or file == "Saviour.py":
                continue

            if os.path.isdir(file):
                continue

            self.targets.append(file)

    def decrypt(self, key_to_decrypt):
        for file in self.targets:
            with open(file, "rb") as target_file:
                cipher = target_file.read()
                plain_text = Fernet(key_to_decrypt).decrypt(cipher)

            with open(file, "wb") as target_file:
                target_file.write(plain_text)

        print("Done.")

    def start(self):
        key = get_key()
        self.gather_targets()
        self.decrypt(key)


Saviour().start()
