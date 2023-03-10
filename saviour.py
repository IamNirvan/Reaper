import os
from cryptography.fernet import Fernet

targets = []


def get_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()


def gather_targets():
    for file in os.listdir():
        if file == "ransom_100.py" or file == "key.key" or file == "saviour.py":
            continue

        if os.path.isdir(file):
            continue

        targets.append(file)


def decrypt(key):
    for file in targets:
        with open(file, "rb") as target_file:
            cipher = target_file.read()
            plain_text = Fernet(key).decrypt(cipher)

        with open(file, "wb") as target_file:
            target_file.write(plain_text)

    print("Done.")


key = get_key()
gather_targets()
decrypt(key)