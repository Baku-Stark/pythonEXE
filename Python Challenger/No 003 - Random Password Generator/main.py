from random import randint

# Lista de caracteres (74 caracteres)
listCarac = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "-", "=", "*", "+", "!", "@", "#", "$", "%", "&", "(", ")"
]

setPassword = ""

for num in range(1, 17):
    randomNum = randint(0, 73)
    setPassword = setPassword + listCarac[randomNum]

print(f"SUA SENHA GERADA É: \033[32m{setPassword}\033[m")