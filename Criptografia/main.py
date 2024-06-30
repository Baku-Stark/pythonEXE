# pip install cryptography

from cryptography.fernet import Fernet

# GERAR UMA CHAVE
key = Fernet.generate_key()
print(key)
with open('./cryptography/key.key', 'a', encoding="utf-8") as keyFile:
    keyFile.write(str(key)[2:-1] + '\n')

fet = Fernet(key)

# ENCRIPTAR MENSAGEM
token = fet.encrypt(b"HEllo")
print(f"TOKEN : {token}")

print(fet.decrypt(token))
keyFile.close()