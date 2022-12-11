import requests
from requests.exceptions import ConnectionError

def internet_connection_test():
    url = "https://github.com/Python-World/python-mini-projects/blob/master/projects/Internet_connection_check/internet_connection_check.py"
    print(f'Tentando conexão com {url}')
    print('')
    print('=' *60)
    try:
        print(url)
        resp = requests.get(url, timeout=10)
        resp.text
        resp.status_code
        letSet = "\033[47m  \033[m"
        statusSucess = "\033[46mConexão feita com sucesso!!\033[m" 
        print(f'{letSet}{statusSucess}')
        print('=' *60)
        return True
    except ConnectionError as e:
        requests.ConnectionError
        letSet = "\033[47m  \033[m"
        statusError = "\033[41mSem conexão...\033[m"
        print(f'{letSet}{statusError}')
        print('=' *60)
        return False
    except:
        letSet = "\033[47m  \033[m"
        statusError = "\033[41mAlgo deu errado...\033[m"
        print(f'{letSet}{statusError}')
        print('=' *60)
        return False

if __name__ == '__main__':
    internet_connection_test()