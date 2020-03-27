"""
Modulo Collections - Default Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

O dafault dict não da KeyErro

Relembrando o dicionario:
dicionario = {'curso': 'Programação em python essencial'}
print(dicionario)
print(dicionario['outro']) # Vai dar erro

Ao criar um dicionario utilizando o default dict, nos informamos um valor default,
podendo utilizar um lambda pra isso. Esse valor será utilizando sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será criada e o valor default
será atribuido

OBS: Lambdas são funções sem nome, que podem ou nao receber os parametros de entrada
e retornar valores.
"""
# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)
print(dicionario['outro'])  # Se fosse no dicionario comum daria KeyError
print(dicionario)


