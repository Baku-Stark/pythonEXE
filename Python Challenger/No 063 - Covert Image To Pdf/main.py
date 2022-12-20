import os
from PIL import Image

try:
    diretio_atual = os. getcwd()
    path_set = rf'{diretio_atual}\No 063 - Covert Image To Pdf\img'
    diretorio = os.listdir(path_set)

    for fname in diretorio:
        # selecionar as imagens da pasta `img`
        image_input = Image.open(rf'{path_set}\{fname}')

        # converter as imagens para PDF
        image_output = image_input.convert('RGB')
        image_output.save(rf'{diretio_atual}\No 063 - Covert Image To Pdf\pdf\convert_{fname}.pdf')
    
    letSet = "\033[47m  \033[m"
    statusSucess = "\033[46m Conversão feita com sucesso!!! \033[m" #Cyan Background
    newSetSucess = f"\033[1m{statusSucess}\033[m"
    print(f"{letSet}{newSetSucess}")

except FileNotFoundError:
    letSet = "\033[47m  \033[m"
    statusError = "\033[41m Diretório não foi encontrado - A conversão não pode ser realizada \033[m" #Red Background
    newSetError = f"\033[1m{statusError}\033[m"
    print(f"{letSet}{newSetError}")