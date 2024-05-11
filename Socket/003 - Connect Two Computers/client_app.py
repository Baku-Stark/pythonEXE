import os
from socket import *

class CLIENT_APP():
    my_socket = socket(AF_INET, SOCK_STREAM)

    def __init__(self, IP_PROXY: str, PORT : int):
        self.__IP_PROXY, self.__PORT = IP_PROXY, PORT

        self.main()

    def main(self):
        # Use a breakpoint in the code line below to debug your script.
        my_socket = socket(AF_INET, SOCK_STREAM)
        my_socket.connect((self.__IP_PROXY, self.__PORT))

        while True:
            user_input = input("Enter your message: ").strip()
            print('')

            my_socket.send(user_input.encode(encoding="utf-8"))

            data = my_socket.recv(1024).decode()
            #print(f"the data is {data}")
            
            if user_input == "EXIT":
                break

        my_socket.close()


if __name__ == '__main__':
    os.system('clear')
    CLIENT_APP("192.168.0.116", 8080)