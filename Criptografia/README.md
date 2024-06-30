# Python - Criptografia

Python é uma linguagem poderosa e versátil que oferece várias bibliotecas para criptografia, como `cryptography`, `PyCrypto`, e `pycryptodome`. Aqui está um exemplo de como usar a biblioteca `cryptography` para criptografar e descriptografar dados.

### Instalação da Biblioteca `cryptography`

Primeiro, instale a biblioteca `cryptography` usando `pip`:

```sh
pip install cryptography
```

### Exemplo de Criptografia Simétrica com Fernet (AES)

O módulo `Fernet` da biblioteca `cryptography` é uma implementação do AES (Advanced Encryption Standard) que oferece uma API simples para criptografia simétrica.

#### Criptografar Dados

1. **Gerar uma Chave de Criptografia**

```python
from cryptography.fernet import Fernet

# Gerar uma chave e salvá-la em um arquivo
key = Fernet.generate_key()
with open('./cryptography/key.key', 'wb') as key_file:
    key_file.write(key)
```

2. **Criptografar uma Mensagem**

```py
# GERAR UMA CHAVE
key = Fernet.generate_key()

# INSERIR KEY NO DOCUMENTO
print(key)
with open('./cryptography/key.key', 'a', encoding="utf-8") as keyFile:
    keyFile.write(str(key)[2:-1] + '\n')

fet = Fernet(key)

# ENCRIPTAR MENSAGEM
token = fet.encrypt(b"HEllo")
print(f"TOKEN : {token}")

print(fet.decrypt(token))
keyFile.close()
```

#### Descriptografar Dados

1. **Descriptografar a Mensagem**

```python
from cryptography.fernet import Fernet

# Carregar a chave
with open('key.key', 'rb') as key_file:
    key = key_file.read()

# Inicializar o objeto Fernet com a chave
cipher_suite = Fernet(key)

# Mensagem criptografada (use a saída do exemplo anterior)
encrypted_message = b'...'

# Descriptografar a mensagem
decrypted_message = cipher_suite.decrypt(encrypted_message)

print(f"Mensagem descriptografada: {decrypted_message}")
```

### Exemplo de Criptografia Assimétrica com RSA

Para criptografia assimétrica, você pode usar a biblioteca `cryptography` para gerar pares de chaves RSA e criptografar/descriptografar dados.

#### Gerar Par de Chaves RSA

```python
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Gerar par de chaves
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Serializar e salvar a chave privada
with open('private_key.pem', 'wb') as key_file:
    key_file.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ))

# Serializar e salvar a chave pública
public_key = private_key.public_key()
with open('public_key.pem', 'wb') as key_file:
    key_file.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))
```

#### Criptografar Dados com a Chave Pública

```python
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Carregar a chave pública
with open('public_key.pem', 'rb') as key_file:
    public_key = serialization.load_pem_public_key(key_file.read())

# Mensagem a ser criptografada
message = b"Esta é uma mensagem secreta"

# Criptografar a mensagem
encrypted_message = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(f"Mensagem criptografada: {encrypted_message}")
```

#### Descriptografar Dados com a Chave Privada

```python
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

# Carregar a chave privada
with open('private_key.pem', 'rb') as key_file:
    private_key = serialization.load_pem_private_key(key_file.read(), password=None)

# Mensagem criptografada (use a saída do exemplo anterior)
encrypted_message = b'...'

# Descriptografar a mensagem
decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(f"Mensagem descriptografada: {decrypted_message}")
```

Esses exemplos mostram como usar a biblioteca `cryptography` em Python para criptografar e descriptografar dados usando criptografia simétrica (AES com Fernet) e criptografia assimétrica (RSA). Dependendo de suas necessidades, você pode escolher o método que melhor se adapta ao seu caso de uso.