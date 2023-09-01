import re

emails = '''
daniel@dominio.com
wallace.freitas@dominio.com
wallace_freitas_1234@dominio.com
gov@dominio.com.br
state@dominio-gov.com.br
estado.rj@gov.br
wallace_freitas@dom-dominio.net
'''

p = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+')
corrs = p.finditer(emails)

for i in corrs:
    print(i)