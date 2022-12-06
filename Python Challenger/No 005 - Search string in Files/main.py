import os

def getFile(text):
    '''
    'r'  -> Usado somente para ler algo;
    'r+' -> Usado para LER e ESCREVER algo;
    'w'  -> Usado somente para escrever algo;
    'w+' -> escrita (o modo w+, assim como o w, também apaga o conteúdo anterior do arquivo);
    'a'  -> Usado para acrescentar algo;
    'a+' -> leitura e escrita (abre o arquivo para atualização)
    '''

    file_name = str(input('   -> Arquivo : '))
    dir_atual = os.getcwd()
    print('-'*60)
    with open(f"{dir_atual}\{file_name}", 'r') as arquivo:
        if text == str(arquivo.read()):
            print(f"Texto encontrado com sucesso!\n -> Diretório do arquivo: {dir_atual}\{file_name}")
        else:
            print('O texto não foi encontrado.')
    print('-'*60)


# =====
text = str(input('Digite o texto : '))
print('')
getFile(text)