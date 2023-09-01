import re

texto = '''
https://www.youtube.com/
https://google.com/
https://www.gov.br/
https://www.estacio.rj.gov.br/
http://www.state.com.br/
'''

p = re.compile(r'https?://(www\.)?([a-zA-Z0-9]+\.)+(com.br|gov.br|com)/')
corrs = p.finditer(texto)

for i in corrs:
    print(i)