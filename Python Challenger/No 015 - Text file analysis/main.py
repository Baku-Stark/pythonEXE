import os
import sys
import collections
import string

from colorama import Fore

script_name = sys.argv[0]

res = {
    "total_lines": "",
    "total_characters": "",
    "total_words": "",
    "unique_words": "",
    "special_characters": ""
}

os.system('cls')

try:
    textfile = sys.argv[1]
    
    with open(textfile, "r", encoding="utf-8") as file_select:
        data = file_select.read()

        res["total_lines"] = len(open(textfile).readlines())
        res["total_characters"] = len(data.replace(" ", ""))

        counter = collections.Counter(data.split())
        d_counter = counter.most_common()

        res["total_words"] = sum([i[1] for i in d_counter])
        res["unique_words"] = len([i[1] for i in d_counter])

        specialChars = string.punctuation

        res["special_characters"] = sum(v for k, v in collections.Counter(data).items() if k in specialChars)

        print('-=' *30)
        print('')
        print(f'-> Diretório: {textfile}\n')
        print(Fore.GREEN + f'{res}')
        print(Fore.RESET)
        print('-=' *30)

except FileNotFoundError:
    print(Fore.RED + f'Não foi possível encontrar o caminho do arquivo [{textfile}]')
    print(Fore.RESET)