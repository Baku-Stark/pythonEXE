import pyperclip

# VAI COPIAR UM TEXTO
pyperclip.copy('Digite o texto aqui')

#  COLAR O TEXTO COPIADO PELO USUÁRIO
spam = pyperclip.paste()
print(spam)