"""
    Profile 
    ---------- 
    Author : Baku - Stark 
    Info   : Application Colors, OperationalSys, CurrentTime. 
"""

import os, argparse
from platform import *
from datetime import datetime

from socket import *
  
class Colors:
    BLACK =     '\033[1;30m'
    RED =       '\033[31m'
    GREEN =     '\033[32m'
    YELLOW =    '\033[33m'
    BLUE =      '\033[34m'
    PURPLE =    '\033[35m'
    CYAN =      '\033[36m'
    WHITE =     '\033[37m'
    GRAY =      '\033[90m'
  
    BACK_RED =       '\033[1;41m'
    BACK_GREEN =     '\033[1;42m'
    BACK_YELLOW =    '\033[1;43m'
    BACK_BLUE =      '\033[1;44m'
    BACK_PURPLE =    '\033[1;45m'
    BACK_CYAN =      '\033[1;46m'
    BACK_WHITE =     '\033[1;47m'
    BACK_GRAY =      '\033[1;40m'
  
    END =       '\033[m'

class OperationalSys:
    @staticmethod
    def clean_console():
        if system() == "Linux":
            os.system("clear")

        else:
            os.system("cls")

class CurrentTime:
    @staticmethod
    def created_at() -> str:
        _data_atual = datetime.now().strftime("%d/%m/%y")
        _hora_atual = datetime.now().strftime("%H:%M")
        return f"{_data_atual} - {_hora_atual}"


class Port_Scanner:
    def __init__(self) -> None:
        self.argparse_init()
        

    def argparse_init(self):
        parser = argparse.ArgumentParser("Port Scanner Applicattion!")

        # [HOST]
        parser.add_argument(
            "host",
            help="Host to scan.",
        )

        # [PORTS]
        parser.add_argument(
            "--ports", "-p",
            dest="port_range",
            default="1-65535",
            help="Port range to scan, default is 1-65535 (all ports)"
        )

        app_args = parser.parse_args()

        start_port, end_port = app_args.port_range.split("-")
        start_port, end_port = int(start_port), int(end_port)

        if start_port < 1:
            start_port = 1

        if end_port > 65535:
            end_port = 65535
        
        print(Colors.BACK_BLUE + f"== Your arguments | {CurrentTime.created_at()} ==" + Colors.END)
        print(Colors.CYAN + f"├── Host : {app_args.host}" + Colors.END)
        print(Colors.CYAN + f"└── Port Range : {start_port} - {end_port}" + Colors.END)

# [test] python main.py 123 --ports 1-500
# learn : https://thepythoncode.com/article/make-port-scanner-python
OperationalSys.clean_console()
Port_Scanner() if __name__ == '__main__' else None