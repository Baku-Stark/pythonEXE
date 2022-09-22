from socket import *

host = gethostname()
port = 55551

cli = socket(AF_INET, SOCK_STREAM)
cli.connect((host, port))

while True:
    msg = input('Mensagem: ')
    cli.send(msg.encode())