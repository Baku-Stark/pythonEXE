from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Gerar par de chaves
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
#print(private_key)

# Serializar e salvar a chave privada
with open('./cryptography/private_key.pem', 'wb') as key_file:
    key_file.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ))
    print("chave (privada) = FEITO!")

# Serializar e salvar a chave pública
public_key = private_key.public_key()
with open('./cryptography/public_key.pem', 'wb') as key_file:
    key_file.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))
    print("chave (pública) = FEITO!")