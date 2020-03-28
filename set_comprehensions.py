"""
Set comprehension

lista = [1, 2, 3, 4, 5]
Set = {1, 2, 3, 4, 5}

"""
# -*- coding: UTF-8 -*-
# Exemplos

numeros = {num for num in range(1, 7)}
print(numeros)

# Outro exemplo

numeros1 = {x ** 2 for x in range(10)}
print(numeros1)

# OBS: faça alteração na estrutura acima para gerar um dicionario ao invés de set:

numeros1 = {x: x ** 2 for x in range(10)}  # So acrescentar o x de chave ja gera o dicionario
print(numeros1)

# Pra finalizar

letras = {letra for letra in "Luan Pinheiro"}
print(letras)  # Não tem repetição
