"""
Entendendo o *args
- O *args é um parametro como outro qualquer. Isso significa que você poderá
chamar de qualquer coisa, desde que comece com asteristico.

Exemplo:

*xis

Mas por converção, utilizamos *args para defini-lo

Mas o que é *args?

O parametro *args utilizado em uma função, coloca os valores extras informados como
entrada em uma tupla. Então desde ja lembre-se que tuplas são imutaveis

# Exemplos


def soma_todos_numeros(num1=1, num2=2, num3=4):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))
# Se passar mais numeros ou menos numeros dá TypeError
"""
# -*- coding: UTF-8 -*-
# Exemplos: entendendo o *args


def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(1, 2))
print(soma_todos_numeros(1, 2, 3))
print(soma_todos_numeros(2, 3, 4, 5, 6))

# Outra forma de fazer
print('\n')


def soma_todos_numeros(*args):
    return sum(args)  # Utilizando a função soma de tuplas


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(1, 2))
print(soma_todos_numeros(1, 2, 3))
print(soma_todos_numeros(2, 3, 4, 5, 6))
# Uma função não precisa só ter o Args


def soma_todos_numeros(nome, email, *args):
    return sum(args)  # Utilizando a função soma de tuplas


print(soma_todos_numeros('Luan', 'Pinheiro'))
print(soma_todos_numeros('Luan', 'Pinheiro', 1))
print(soma_todos_numeros('Luan', 'Pinheiro', 1, 2))
print(soma_todos_numeros('Luan', 'Pinheiro', 1, 2, 3))
print(soma_todos_numeros('Luan', 'Pinheiro', 2, 3, 4, 5, 6))
print('\n')


# Outro exemplo de utilização do Args (MUITO UTIL)


def verifica_info(*args):
    if 'Luan' in args and 'Pinheiro' in args:  # Se Luan estiver contido em args e Pinheiro estiver contido tbm retorne.
        return 'Bem vindo Luan'
    return 'Eu não tenho certeza de quem você é'


print(verifica_info())
print(verifica_info(1, True, 'Luan', 'Pinheiro'))
print(verifica_info(1, 'Luan', 3.145))
print(verifica_info('Luan', 'Pinheiro'))
print('\n')

# --------------------------------------------------


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(1, 2, 3, 4))

numeros = [1, 2, 3, 4, 5]
print(soma_todos_numeros(*numeros))  # utilizando asteristico para desempacotar

"""
OBS: O asteristico serve para que informemos ao python que estamos 
passando como argumento uma coleção de dados, dessa forma ele saberá
que precisara antes desempacotar os dados
"""


