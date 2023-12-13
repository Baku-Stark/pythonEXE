import re

emails = '''
daniel@dominio.com
wallace.freitas@dominio.com
wallace_freitas_1234@dominio.com
gov@dominio.com.br
state@dominio-gov.com.br
estado.rj@gov.br
wallace_freitas@dom-dominio.net
milena@hotmail.com.br
'''

p = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(.[A-Z|a-z]{2,})+')
corrs = p.finditer(emails)

for i in corrs:
    print(i)