"""
Regular Expressions (Regex) - Python
------

Documentation: https://docs.python.org/3/library/re.html
"""

import re

# .  -> Entende qualquer valor exceto uma nova linha
# \. -> Para buscar o caracter "."
print("=== STEP 1 ===")
text_step_1 = "arara"
padrao = re.compile("ar.ra")
check = padrao.findall(text_step_1)

print(check)
print('')

# ^   -> Irá testar o início da string  
# [^] -> Irá considerar todos os caracteres EXCETO o indicado
print("=== STEP 2 ===")
text_step_2 = "arara"
p2 = re.compile("^a")
p2_1 = re.compile("[^a]")
check_2 = p2.findall(text_step_2)
check_2_1 = p2_1.findall(text_step_2)

print(check_2)
print(check_2_1)
print('')

# \d -> Qualquer caracter que SEJA um algoritmo de 0 a 9
# \D -> Qualquer caracter que NÃO SEJA um algoritmo de 0 a 9
print("=== STEP 3 ===")
text_step_3 = "arara1992"
p3 = re.compile(r"\d")
p3_1 = re.compile(r"\D")
check_3 = p3.findall(text_step_3)
check_3_1 = p3_1.findall(text_step_3)

print(check_3)
print(check_3_1)
print('')

# \s -> Qualquer caracter que SEJA vazio
# \S -> Qualquer caracter que NÃO SEJA vazio
print("=== STEP 4 ===")
text_step_4 = """

arara 1992

"""
p4 = re.compile(r"\s")
p4_1 = re.compile(r"\S")
check_4 = p4.findall(text_step_4)
check_4_1 = p4_1.findall(text_step_4)

print(check_4)
print(check_4_1)
print('')

# \w -> Qualquer caracter que SEJA alfanumérico
# \W -> Qualquer caracter que NÃO SEJA alfanumérico
print("=== STEP 5 ===")
text_step_5 = """

_arara 1992_

"""
p5 = re.compile(r"\w")
p5_1 = re.compile(r"\W")
check_5 = p5.findall(text_step_5)
check_5_1 = p5_1.findall(text_step_5)

print(check_5)
print(check_5_1)
print('')