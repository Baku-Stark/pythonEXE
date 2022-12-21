while True:
    numSelect = int(input('Escolha um número para para fazer a conversão\nr: '))
    print('')
    if numSelect < 1:
        print('Valor incorreto!')
    else:
        print(
            f"""
            + Conversão para Binário:
            |   --------------------------------
            |   Número escolhido: \033[32m{numSelect}\033[m
            |   Número convertido para binário: \033[32m{bin(numSelect)[2:]}\033[m
            +-+---------------- x ----------------
            """
        )
        print(
            f"""
            + Conversão para Decimal:
            |   Número escolhido: \033[32m{numSelect}\033[m
            |   --------------------------------
            |   Número convertido para Decimal(10): \033[32m{numSelect/10}\033[m
            |   Número convertido para Decimal(100): \033[32m{numSelect/100}\033[m
            |   Número convertido para Decimal(1000): \033[32m{numSelect/1000}\033[m
            +-+---------------- x ----------------
            """
        )
    print('-'*80)
    res = str(input('Deseja fazer outra conversão?  (SIM/NÃO)\nr: ')).upper()

    if res == 'SIM':
        print('-'*80)
        letSet = "\033[47m  \033[m"
        statusSucess = "\033[42m Nova Conversão! \033[m" #Green Background
        newSetSucess = f"\033[1m{statusSucess}\033[m"
        print(f"{letSet}{newSetSucess}")
        continue
    else:
        letSet = "\033[47m  \033[m"
        statusSucess = "\033[46m Programa ENCERRADO! \033[m" #Cyan Background
        newSetSucess = f"\033[1m{statusSucess}\033[m"
        print(f"{letSet}{newSetSucess}")
        break