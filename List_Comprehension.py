"""
List Comprehension - Parte 1

- Utilizando list comprehension nos podemos gerar novas listas com dados processados
a partir de outro iteravel

# Sintaxe da list comprehensions
[] - sempre começa com colchete

[ dado for dado in iteravel] para cada dado nessa lista de dado faça isso
"""
# -*- coding: UTF-8 -*-
# Exemplo:

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]
# Acima é dito: Para cada numero da lista multiplica por 10 e faça uma nova lista
print(res)

"""
Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:
- A primeira parte: for numero in numeros
- Segunda parte: numero * 10
"""

res = [numero / 2 for numero in numeros]
print(res)

# Fazendo em uma função
print('\n')


def funcao (valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)
print('\n')
# ----------------------------------------------------------

# List comprehension versus loop
# Loop
numeros = [1, 2, 3, 4, 5, 6]
numeros_dobrados = []

for numero in numeros:
    numero_dobrados = numero * 2
    numeros_dobrados.append(numero_dobrados)

print(numeros_dobrados)

# Agora com List comprehensions
print([numero * 2 for numero in numeros])
# MUITO MAIS FACIL

print('\n')
# -------------------------------------------
# Outros exemplos

nome = 'Luan Pinheiro'

print([letra.upper() for letra in nome])

# exemplo 2:


def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['Luan', 'Hulk', 'Viviane', 'Maria', 'Francisco', 'Stela']

print([caixa_alta(amigo) for amigo in amigos])


# Exemplo 3

print([numero * 3 for numero in range(1 , 10)])

# Exemplo 4
print('\n')

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# Exemplo 5
print('\n')

print([str(numero) for numero in [1, 2, 3, 4, 5]])
