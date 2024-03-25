import os

# import necessary modules
from pathlib import Path
from zipfile import ZipFile
from tqdm import tqdm #pip install tqdm - https://tqdm.github.io/

from services.__COLORS import Colors
from services.__TempPrint import TempPrint

os.system('cls')
# import the word-list
passwords_file = Path(str(input('[0] Word List Path: ')))
zip_file_path = Path(str(input('[1] Zip File Path: ')))

def crack_password():
    zip_file = ZipFile(zip_file_path)
    
    # count the number of word in the file (pass.txt)
    num_pass = len(list(open(passwords_file, 'rb')))
    # print(num_pass)

    # open file and loop (for)
    pass_file = open(passwords_file, 'rb')

    for password in tqdm(pass_file, total=num_pass, unit='password'):
        TempPrint(Colors.CYAN + f"\n[ - ] Current password: {password.decode().strip()}"  + Colors.END).TPrint()

        try:
            zip_file.extractall(pwd=password.strip(), path='output')

        except Exception as error:
            continue
        
        else:
            print(Colors.GREEN + f'[ - ] Password found! [{password.decode().strip()}]' + Colors.END)
            exit(0)

    print(Colors.RED + '[ x ] Password not found, try other wordlist...' + Colors.END)


if __name__ == '__main__':
    if passwords_file.exists() and zip_file_path.exists():
        print(Colors.GREEN + '[ - ] Path found!' + Colors.END)
        print('')
        
        crack_password()

    else:
        print(Colors.RED + '[ x ] An incorrect or non-existent path was entered...' + Colors.END)
        exit(1)