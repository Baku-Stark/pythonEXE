import socket  
import sys  

# Verifique se a porta foi passada como argumento  
if len(sys.argv) != 2:  
    print("Uso: python servidor.py <PORTA>")  
    sys.exit(1)  

# Captura a porta do argumento  
PORT = int(sys.argv[1])  
HOST = '0.0.0.0'  # Aceita conexões de qualquer IP  

# Crie um socket  
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
servidor.bind((HOST, PORT))  
servidor.listen(1)  

print(f"Servidor escutando em {HOST}:{PORT}...")  

while True:  
    conexao, endereco = servidor.accept()  
    print(f"Conexão estabelecida por {endereco}")  
    mensagem = "Olá, cliente!"  
    conexao.sendall(mensagem.encode('utf-8'))  
    conexao.close()
