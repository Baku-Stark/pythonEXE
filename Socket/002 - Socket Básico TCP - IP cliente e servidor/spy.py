from re import I
from socket import *

host = gethostname()
port = 55551

print(f'HOST: {host}\nPORT: {port}')

serv = socket(AF_INET, SOCK_STREAM)
serv.bind((host, port))
serv.listen(5)

while True:
    con, adr = serv.accept()
    while True:
        msg = con.recv(1024)
        msg.decode()