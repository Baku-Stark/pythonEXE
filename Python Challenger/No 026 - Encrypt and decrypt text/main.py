# IMPORT [pip install colorama]
from colorama import Fore

# IMPORT
import base64
import sys
import os

class CryptographySYS():
    def __init__(self):
        '''
            Start of application\n
            ├── Return:
                ├── filePath : Variable that will hold the text
                └── key : generate a key for encryption and decryption
        '''
        self.filePath = sys.argv[1]

        # ---- [FUNCTIONS]
        print('-=' *50)
        print('RESULTADO DA CRIPTOGRAFIA:')
        print('')
        self.cryptFileText(self.filePath)
        print('')
        print('-=' *50)

    def cryptFileText(self, filePath):
        '''
            Encryption function
            ├── Args:
                ├── filePath : User chosen file path
        '''

        self.encMESSAGE = None

        with open(filePath, 'r') as fileText:
            # 'r'  -> Usado somente para ler algo;
            # 'r+' -> Usado para LER e ESCREVER algo;
            # 'w'  -> Usado somente para escrever algo;
            # 'w+' -> escrita (o modo w+, assim como o w, também apaga o conteúdo anterior do arquivo);
            # 'a'  -> Usado para acrescentar algo;
            # 'a+' -> leitura e escrita (abre o arquivo para atualização)
            message = fileText.read()
            self.crypt_message = base64.b64encode(message.encode("ascii", "strict"))

            self.encMESSAGE = self.crypt_message

        print('Texto criptografado: ' + Fore.CYAN + str(self.encMESSAGE) + Fore.RESET)
        self.decryptFileText(self.encMESSAGE)

    def decryptFileText(self, filePath):
        '''
            Decryption function
            ├── Args:
                └── filePath : User chosen file path
        '''

        message = base64.b64decode(filePath)

        self.decrypt_message = message.decode("ascii", "strict")

        print('Texto descriptografado: ' + Fore.BLUE + str(self.decrypt_message) + Fore.RESET)


#  =============================
# APP
if __name__ == '__main__':
    os.system('cls')
    CryptographySYS()