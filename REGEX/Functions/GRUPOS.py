import re

texto = '''
Arara 1992
arara 1993
'''

p = re.compile(r'(A|a)?[a-z]{4} [0-9]+')
corrs = p.finditer(texto)

for i in corrs:
    print(i.group(0)) # mostra a string inteira
    print(i.group(1)) # mostras apenas o primeiro caracter da string