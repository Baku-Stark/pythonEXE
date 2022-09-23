from socket import *

serv = socket(AF_INET, SOCK_STREAM)
serv.connect((gethostname(), 55551))

while True:
    msg = input('Message: ')
    serv.send(msg.encode())