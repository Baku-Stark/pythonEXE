def saveLinks(site_name, link):
    '''
    'r'  -> Usado somente para ler algo;
    'r+' -> Usado para LER e ESCREVER algo;
    'w'  -> Usado somente para escrever algo;
    'w+' -> escrita (o modo w+, assim como o w, também apaga o conteúdo anterior do arquivo);
    'a'  -> Usado para acrescentar algo;
    'a+' -> leitura e escrita (abre o arquivo para atualização)
    '''

    if ("https" or "http") in link:
        print('Endereçamento de domínio correto. Adicionado ao arquivo \033[32m[SaveLinks.txt]\033[m')
        link_set = f"[{site_name}]({link})"
        with open('SaveLinks.txt', 'a+') as arq:
            arq.write(f"{link_set}\n")
    else:
        print('Endereçamento de domínio incorreto')

# ===
site_name = str(input('Nome do site : '))
link = str(input('URL do site : '))
print('')
saveLinks(site_name, link)