# Função pra fazer a verificação
# -*- coding: UTF-8 -*-


def verifica_info(*args):
    if 'Luan' in args and 'Pinheiro' in args:
        return 'Bem vindo Luan'
    return 'Eu não tenho certeza de quem você é, favor verificar cadastro'


pessoa = input('Bem vindo identifique seu primeiro nome: \n')
print(pessoa)
ultimo = input('Agora escreva seu ultimo nome: \n')
print(verifica_info(pessoa, ultimo))
