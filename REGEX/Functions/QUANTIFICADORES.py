import re

text = '''
Arara
'''

# * -> 0 ou mais =====
p = re.compile(r'[ra]*')

corrs = p.finditer(text)

for i in corrs:
    print(i)

# === OUTPUT
# <re.Match object; span=(0, 0), match=''>
# <re.Match object; span=(1, 1), match=''>
# <re.Match object; span=(2, 6), match='rara'>
# <re.Match object; span=(6, 6), match=''>
# <re.Match object; span=(7, 7), match=''>
print("=" *30)

#  =============================================
# + -> 1 ou mais =====
p = re.compile(r'[ra]+')

corrs = p.finditer(text)

for i in corrs:
    print(i)
# === OUTPUT
# <re.Match object; span=(2, 6), match='rara'>
print("=" *30)

#  =============================================
# ? -> 0 ou um =====
p = re.compile(r'[ra]?')

corrs = p.finditer(text)

for i in corrs:
    print(i)
# === OUTPUT
# <re.Match object; span=(0, 0), match=''>
# <re.Match object; span=(1, 1), match=''>
# <re.Match object; span=(2, 3), match='r'>
# <re.Match object; span=(3, 4), match='a'>
# <re.Match object; span=(4, 5), match='r'>
# <re.Match object; span=(5, 6), match='a'>
# <re.Match object; span=(6, 6), match=''>
# <re.Match object; span=(7, 7), match=''>
print("=" *30)

#  =============================================
# {3} -> número exato de repetições =====
p = re.compile(r'[ra]{2}')

corrs = p.finditer(text)

for i in corrs:
    print(i)
# === OUTPUT
# <re.Match object; span=(2, 4), match='ra'>
# <re.Match object; span=(4, 6), match='ra'>
print("=" *30)

#  =============================================
# {3,4} -> de 3 a 4 min e max =====
p = re.compile(r'[ra]{2,4}')

corrs = p.finditer(text)

for i in corrs:
    print(i)
# === OUTPUT
# <re.Match object; span=(2, 6), match='rara'>
print("=" *30)