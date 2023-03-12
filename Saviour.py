from cryptography.fernet import Fernet
from threading import Thread


def get_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()


class Saviour(Thread):
    def __init__(self, targeted_files):
        super().__init__()
        self.targets = targeted_files

    def decrypt(self, key):
        try:
            for file in self.targets:
                with open(file, "rb") as target_file:
                    cipher = target_file.read()
                    plain_text = Fernet(key).decrypt(cipher)

                with open(file, "wb") as target_file:
                    target_file.write(plain_text)

        except Exception as e:
            print(f"An error occurred:\n\t{e.__str__()}")


    def run(self):
        key = get_key()
        self.decrypt(key)


if __name__ == "__main__":
    # targets = ['C:\\Users\\Shalin\\Documents\\3_Python\\Python_projects\\Reaper\\test files\\document.docx',
    #            'C:\\Users\\Shalin\\Documents\\3_Python\\Python_projects\\Reaper\\test files\\main.py',
    #            'C:\\Users\\Shalin\\Documents\\3_Python\\Python_projects\\Reaper\\test files\\quaterlyStats.elsx',
    #            'C:\\Users\\Shalin\\Documents\\3_Python\\Python_projects\\Reaper\\test files\\recipies.txt',
    #            'C:\\Users\\Shalin\\Documents\\3_Python\\Python_projects\\Reaper\\test files\\private\\searches.txt',
    #            'C:\\Users\\Shalin\\Documents\\3_Python\\Python_projects\\Reaper\\test files\\private\\sdcs\\Doodoo']

    Saviour(targets).start()
