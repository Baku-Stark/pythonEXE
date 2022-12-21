import socket

def get_hostname_IP():
    hostname = str(input('Insira o URL do site\nr: '))
    print('')
    if (".com") not in hostname:
        letSet = "\033[47m  \033[m"
        statusError = "\033[41m URL de site inválido \033[m" #Red Background
        newSetError = f"\033[1m{statusError}\033[m"
        print(f"{letSet}{newSetError}")
        quit()
    
    try:
        print(
            f"""
            + INFORMAÇÕES:
            |   --------------------------------
            |   Hostname: \033[32m{hostname}\033[m
            |   IP: \033[32m{socket.gethostbyname(hostname)}\033[m
            +-+---------------- x ----------------
            """
        )
    except socket.gaierror as error:
        letSet = "\033[47m [ERROR] \033[m"
        statusError = f"\033[41m {error} \033[m" #Red Background
        newSetError = f"\033[1m{statusError}\033[m"
        print(f"{letSet}{newSetError}")

if __name__ == '__main__':
    get_hostname_IP()