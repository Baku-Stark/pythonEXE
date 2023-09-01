import re

print("=== MATCH ===")
text_match_1 = "arara"
mp_1 = re.compile(r"ar")
check_findall_1 = mp_1.findall(text_match_1)
check_match_1 = mp_1.match(text_match_1)
check_search_1 = mp_1.search(text_match_1)
check_finditer_1 = mp_1.finditer(text_match_1)

print(check_findall_1)

print(check_match_1) # -> Procura no INÍCIO da string
print(check_search_1) # -> Procura por TODA a string

print(check_finditer_1) # -> <callable_iterator object at 0x0000021D14247CD0>
corrs = check_finditer_1
for i in corrs:
    print(i)
    # <re.Match object; span=(0, 2), match='ar'>
    # <re.Match object; span=(2, 4), match='ar'>

print(text_match_1[0:2])