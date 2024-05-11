import os
from socket import *

class SERVER_APP():
    def __init__(self, IP_PROXY: str, PORT : int):
        self.__IP_PROXY, self.__PORT = IP_PROXY, PORT

        self.__SERVER_SOCKET = socket(AF_INET, SOCK_STREAM)

        print('\033[36m' + "=== WELCOME TO F.R.I.D.A.Y ===" + '\033[m')
        self.main()

    def main(self):
        self.__SERVER_SOCKET.bind((self.__IP_PROXY, self.__PORT))
        self.__SERVER_SOCKET.listen()

        (proxy_socket, proxy_address) = self.__SERVER_SOCKET.accept()
        print(f"[-] Client on - {proxy_address[0]}")
        print('\n' * 3)

        while True:
            data = proxy_socket.recv(1024).decode() # mensagem do cliente

            data_to_proxy = data.encode()
            message = str(data_to_proxy)[2:-1]
            
            proxy_socket.send(data_to_proxy)
            

            if message == "EXIT":
                break
            
            else:
                print(f"""-- Message: {data}""")

        proxy_socket.close()
        self.__SERVER_SOCKET.close()

if __name__ == '__main__':
    os.system('clear')
    SERVER_APP("192.168.0.116", 8080)