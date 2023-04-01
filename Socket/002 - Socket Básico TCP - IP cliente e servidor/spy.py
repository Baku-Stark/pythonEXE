from socket import *

serv = socket(AF_INET, SOCK_STREAM)
serv.bind((gethostname(), 55551))
serv.listen(5)

print('=== F.R.I.D.A.Y SYSTEM===')

while True:
    con, adr = serv.accept()
    
    print(f"Connection (IP Private: {adr[0]}) has been established!")

    con.send(bytes("Welcome to F.R.I.D.A.Y server!!!", "utf-8"))
    print('')

    while True:
        user = con.recv(1024)
        user = user.decode()

        msg = con.recv(1024)
        msg = msg.decode()

        print(f'{user}*: {msg}')