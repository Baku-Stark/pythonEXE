import socket  
import sys  

# Verifique se a IP e a porta foram passados como argumento  
if len(sys.argv) != 3:  
    print("Uso: python cliente.py <IP_DO_LINUX> <PORTA>")  
    sys.exit(1)  

# Captura ip e a porta do argumento  
HOST = sys.argv[1]  # IP do servidor  
PORT = int(sys.argv[2])  # A porta do servidor  

# Crie um socket  
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

try:  
    cliente.connect((HOST, PORT))  

    # Receba a mensagem do servidor  
    mensagem = cliente.recv(1024)  
    print(f"Mensagem do servidor: {mensagem.decode('utf-8')}")  
except ConnectionRefusedError:  
    print("Conexão recusada. Verifique se o servidor está rodando e a porta está correta.")  
except Exception as e:  
    print(f"Ocorreu um erro: {e}")  
finally:  
    # Feche a conexão  
    cliente.close()
