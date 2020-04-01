"""
Criptografando

"""
from passlib.hash import pbkdf2_sha256 as cript

texto = cript.hash('Encriptografando o texto')
print(texto)

# TESTE DE CONFIRMAÇÃO DE SENHAS

confirmando1 = cript.verify('Encriptografando o texto', texto)  # Igual
print(confirmando1)
confirmando2 = cript.verify('diferente', texto)  # diferente
print(confirmando2)

