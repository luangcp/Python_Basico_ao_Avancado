"""
Any e All

all() -> Retorna True: se todos os elementos do iteravel são verdadeiros ou o iteravel ta vazio

any() -> Retorna True se qualquer elemento do iteravel for verdadeiro. Se o iteravel estiver
vazio, retorna false

"""
# -*- coding: UTF-8 -*-
# Exemplo all()

print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiro? False o 0 não é
print(all([1, 2, 3, 4]))  # Verdadeiro
print(all([]))  # Verdadeiro
print(all('Luan'))  # Verdadeiro
print('\n')
nomes = 'Luan', 'Lucio', 'Luciano', 'Liliane'
print(all([nome[0] == 'L' for nome in nomes]))

nomes = 'Luan', 'Lucio', 'Luciano', 'Liliane', 'Daniel'
print(all([nome[0] == 'L' for nome in nomes]))

print(all([letra for letra in 'eio' if letra in 'aeiou']))  # Vendo se essas letras tao ai dentro
print('\n')

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))  # Se todos for par ou a coleção for vazia retorna true
print('\n')
# ---------------------------------------------------------------------------------
# eexemplos any
# Basta ter um verdadeiro pra ser true
print(any([0, 1, 2, 3, 4]))  # True
print(any([0, False, {}, 0, False]))  # False

