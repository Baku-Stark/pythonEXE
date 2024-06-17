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
import concurrent.futures
  
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
            default=1024,
            help="Port range to scan, default is 1-65535 (all ports)"
        )

        app_args = parser.parse_args()

        print(Colors.BACK_BLUE + f"== Port Scanner | {CurrentTime.created_at()} ==" + Colors.END)
        print(Colors.CYAN + f"├── Host : {app_args.host}" + Colors.END)
        print(Colors.CYAN + f"└── Port Range : 1 - {app_args.port_range}" + Colors.END)
        print('\n' * 2)

        #65536
        ports = self.port_scan(app_args.host, range(1, int(app_args.port_range) + 1))
        if not ports:
            print(Colors.RED + "Nenhuma porta aberta..." + Colors.END)

        else:
            for port_number in ports:
                print(Colors.GREEN + "● " + Colors.END + f"Host ({app_args.host}) port - {port_number} : open")

    def scan_port(self, host, port):
        try:
            sock = socket(AF_INET, SOCK_STREAM)

            sock.settimeout(1)

            result = sock.connect_ex((host, port))

            if result == 0:
                return port, True
            
            else:
                return port, False
        
        except Exception as e:
            return port, False

    def port_scan(self, host, ports, workers=10):
        open_ports = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            # Mapeia a função scan_port para cada porta na lista de portas
            future_to_port = {executor.submit(self.scan_port, host, port): port for port in ports}

            for future in concurrent.futures.as_completed(future_to_port):
                port = future_to_port[future]
                
                try:
                    port_result = future.result()
                    if port_result[1]:
                        open_ports.append(port_result[0])
                
                except Exception as e:
                    print(f"Erro ao escanear porta {port}: {e}")
        
        return open_ports

# [test] python main.py 123 --ports 1-500
# learn : https://thepythoncode.com/article/make-port-scanner-python
OperationalSys.clean_console()
Port_Scanner() if __name__ == '__main__' else None