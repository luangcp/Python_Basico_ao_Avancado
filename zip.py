"""
Zip

zip() - Ele cria um iteravel (zip object) que agrega elemento de cada um dos iteraveis
passados como entrada em pares.

"""
# -*- coding: UTF-8 -*-
# Exemplos:

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)  # Pega o primeiro elemento de cada uma das lista, o segundo e assim por diante

print(list(zip1))
print(type(zip1))

# Sempre podemos gerar uma lista. Tupla ou dicionario
zip1 = zip(lista1, lista2)
print(tuple(zip1))
zip1 = zip(lista1, lista2)
print(set(zip1))
zip1 = zip(lista1, lista2)
print(dict(zip1))

"""
OBS: o zip utiliza como parametro o menor tamenho em iteravel. Isso significa
que se estiver trabalhando com iteraveis de tamanhos diferentes, ira parar 
quando os elementos do menor iteravel acabar
"""
lista3 = (7, 8, 9, 10, 11)

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))

print('\n')

# Podemos utilizar diferentes iteraveis com zip

tupla = 1, 2, 3, 4, 5
lista4 = [6, 7, 8, 9]

zt = zip(tupla, lista4)

# Lista de tuplas

dados = [(0,1), (2,3), (4,5)]
print(list(zip(*dados)))

# Exemplos mais complexos:
# Relacionar nota com as pessoas:
prova1 = [88, 89, 100]
prova2 = [33, 12, 98]
alunos = ['Luan', 'Viviane', 'Hulk']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# Podemos utilizar o map():

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))
