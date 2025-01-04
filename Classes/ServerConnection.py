import socket

import Configuration
from Classes.Connection import Connection
from Configuration import server

ip, port = server["ip"], server["port"]

from colorama import Fore;
from colorama import Back;

class ServerConnection:
    def __init__(self, address):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if Configuration.settings["DisableNagle"] == True:
            self.server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
        self.setupConnection(address)

    def setupConnection(self, address):
        self.server.bind(address)
        print(f"{Back.WHITE}{Fore.BLACK}V43{Fore.MAGENTA}{Back.RESET} ME\033[38;5;208mB{Fore.WHITE}S{Fore.YELLOW}+ {Fore.RESET}| {Fore.CYAN}{ip} {Fore.GREEN}:{Fore.BLUE} {port}{Fore.RESET}")
        while True:
            self.server.listen()
            socket, address = self.server.accept()
            print(f"{Fore.GREEN}[!]{Fore.WHITE} Connect:{Fore.CYAN}", address[0], f":{Fore.BLUE}", address[1], f"{Fore.RESET}")
            Connection(socket, address).start()