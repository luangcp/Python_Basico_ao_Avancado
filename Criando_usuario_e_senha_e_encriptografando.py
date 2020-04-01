"""
Programa: Criando um usuario e senha, confirmando a senha para criar, e encriptografar
Autor: Luan Pinheiro
"""
from passlib.hash import pbkdf2_sha256 as cryp  # Biblioteca de encriptografar
import os
import time


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__sobrenome = sobrenome
        self.__nome = nome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=20000, salt_size=16)

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
usuario = input('Informe o nome de usuario desejado: ')
email = input('Informe o email: ')
senha = input('Informe o senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere..')
    exit(42)


print(f' Seja bem-vindo {nome}\n Usuario criado com sucesso!\n seu email:{email}\n Seu nome de usuario\n {usuario}')

usuario = input('Informe o nome de usuario para acesso: ')
senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Bem vindo {usuario} \na sua Senha criptografada é: {user._Usuario__senha}')