""""
Min e Max

max() -> Retorna o maior valor de um iteravel ou o maior de dois ou mais elementos.

min() -> Retorna o menor valor em um iteravel ou o menor de dois ou mais elementos
"""
# -*- coding: UTF-8 -*-
# Exemplos Max

tupla = 1, 2, 3, 4, 5, 99, 188, 2, -4, 44, 54, 542, 12
print(max(tupla))

lista = [1, 2, 3, 4, 5, 99, 188, 2, -4, 44, 54, 542, 12]
print(max(lista))

conjunto = {1, 2, 3, 4, 5, 99, 188, 2, -4, 44, 54, 542, 12}
print(max(conjunto))

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 99,
              'g': 188, 'h': 2, 'i':-4, 'j': 44, 'k': 54, 'l': 542, 'm': 12}
print(max(dicionario))  # Se passar so dicionario ele passa a maior chave
print(max(dicionario.values()))  # Aqui passa o maior valor em numeros

# ---------------------------------------------------------------------------
print('\n')
# Outros exemplos de max
# Faça um programa que receba dois valores do usuario e mostre o valor
val1 = int(input('Informe o primeiro valor: \n'))
val2 = int(input('Informe o segundo valor: \n'))

print(max(val1, val2))

# Outro
print(max('a', 'abc', 'abcd'))

# Outro
print(max('Luan Pinheiro'))

# Outro
print(max(3.22, 4.123, 4.1))
print('\n')
# --------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------


# Exemplos sobre Min

tupla = 1, 2, 3, 4, 5, 99, 188, 2, -4, 44, 54, 542, 12
print(min(tupla))

lista = [1, 2, 3, 4, 5, 99, 188, 2, -4, 44, 54, 542, 12]
print(min(lista))

conjunto = {1, 2, 3, 4, 5, 99, 188, 2, -4, 44, 54, 542, 12}
print(min(conjunto))

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 99,
              'g': 188, 'h': 2, 'i': -4, 'j': 44, 'k': 54, 'l': 542, 'm': 12}
print(min(dicionario))  # Se passar so dicionario ele passa a menor chave
print(min(dicionario.values()))  # Aqui passa o menor valor em numeros


print('\n')

# Outros exemplos de min
# Faça um programa que receba dois valores do usuario e mostre o menor valor
val1 = int(input('Informe o primeiro valor: \n'))
val2 = int(input('Informe o segundo valor: \n'))

print(min(val1, val2))

# Outro
print(min('a', 'abc', 'abcd'))

# Outro
print(min('Luan Pinheiro'))

# Outro
print(min(3.22, 4.123, 4.1))
print('\n')


# Exemplos mais complexos

nomes = ['Luan', 'Viviane', 'Hulk', 'Stela',
         'Francisco', 'Liliane', 'Cleiton', 'Liliane']

print(max(nomes))  # Ordem alfabetica: Viviane
print(min(nomes))  # Ordem alfabetica: Cleiton

# Como fazer pelo tamanho do nome??
print(max(nomes, key=lambda nome: len(nome)))  # Francisco
print(min(nomes, key=lambda nome: len(nome)))  # Luan

print('\n \n')

# Lista de musicas

musicas = [
    {"titulo": "Graveto", "Tocou": 8},
    {"titulo": "Largado as traças", "Tocou": 5},
    {"titulo": "Infiel", "Tocou": 7},
    {"titulo": "Gelo", "Tocou": 3},
    {"titulo": "Nocaute", "Tocou": 7}
]

# Musica que mais tocou
print(max(musicas, key=lambda musica: musica['Tocou']))
# Musica que menos tocou
print(min(musicas, key=lambda musica: musica['Tocou']))

# DESAFIO: Imprima somente o titulo da musica mais e menos tocada
print(max(musicas, key=lambda musica: musica['Tocou']))
# Musica que menos tocou
print(min(musicas, key=lambda musica: musica['Tocou']))

# Desafio, como encontrar a musica mais tocada e a menos tocada sem usar max() e min() e lambda?

max = 0
for musica in musicas:
    if musica['Tocou'] > max:
        max = musica['Tocou']

for musica in musicas:
    if musica['Tocou'] == max:
        print(musica['titulo'])

min = 99999999
for musica in musicas:
    if musica['Tocou'] < min:
        min = musica['Tocou']

for musica in musicas:
    if musica['Tocou'] == min:
        print(musica['titulo'])