import re

#  =============================================
# CHARACTER SET
CHARACTER_SET_TEXT = '''
Arara 1992
'''

p_set = re.compile(r'[a-zA-Z0-9]') # pegar apenas os valores determinados dentro do array
corrs = p_set.finditer(CHARACTER_SET_TEXT)

for i in corrs:
    print(i)

# === OUTPUT

# <re.Match object; span=(1, 2), match='A'>
# <re.Match object; span=(2, 3), match='r'>
# <re.Match object; span=(3, 4), match='a'>
# <re.Match object; span=(4, 5), match='r'>
# <re.Match object; span=(5, 6), match='a'>
# <re.Match object; span=(7, 8), match='1'>
# <re.Match object; span=(8, 9), match='9'>
# <re.Match object; span=(9, 10), match='9'>
# <re.Match object; span=(10, 11), match='2'>

#  =============================================
# CHARACTER SET [2]
CHARACTER_SET_TEXT_2 = '''
Arara 1992
'''

p_set = re.compile(r'[a-zA-Z] [0-9]') # pegar apenas os valores determinados dentro do array
corrs = p_set.finditer(CHARACTER_SET_TEXT_2)

for i in corrs:
    print(i)

# <re.Match object; span=(5, 8), match='a 1'>

#  =============================================
# CHARACTER SET [3]
CHARACTER_SET_TEXT_3 = '''
Arara 1992
'''

p_set = re.compile(r'[a-zA-Z]+ [0-9]+') # pegar apenas os valores determinados dentro do array
corrs = p_set.finditer(CHARACTER_SET_TEXT_3)

for i in corrs:
    print(i)

# <re.Match object; span=(1, 11), match='Arara 1992'>