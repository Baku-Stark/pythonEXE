import os
from socket import *

serv = socket(AF_INET, SOCK_STREAM)
serv.connect((gethostname(), 55551))

while True:
    user = os.getlogin()
    msg = input('Message: ')

    serv.send(user.encode())
    serv.send(msg.encode())