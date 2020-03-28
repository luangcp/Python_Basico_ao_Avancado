"""
Dictionary Comprehension

Pense no seguinte:
Se quisermos criar uma lista fazemos:

lista = [1, 2, 3, 4, 5]

Se quisermos criar uma tupla:

tupla = 1, 2, 3, 4, 5 ou (1, 2, 3, 4, 5)

se quisermos criar um set (conjunto)
conjuntos = {1, 2, 3, 4, 5}

se quisermos criar um dicionario:
dicionario = {'a' : 1, 'b': 2, 'c': 3}

# Sintaxy

{chave:valor for valor in iteravel}

comparando com lista:
[valor for valor in iteravel]

* Muda a questão de bibliotecas usar chave:valor
"""
# -*- coding: UTF-8 -*-

# Exemplos:

numeros = {'a': 1, 'b': 2, 'c': 3}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)
print('\n')
# Exemplo 2:

numeros1 = [1, 2, 3, 4, 5]  # Funciona se for qualquer coisa, tupla set conjunto lista, qualquer um

quadrados1 = {valor: valor ** 2 for valor in numeros1}

print(quadrados1)

# Em dicionarios não pode ter repetição LEMBRAR

# Exemplo 3
print('\n')

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

print('\n')
# Exemplos com logica condicional

numeros = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)