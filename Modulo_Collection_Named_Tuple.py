"""
Modulo Collection Named Tuple

Recapitulando:
tupla = (1, 2, 3)
print(tupla[1])

Named Tuple -> São tuplas diferenciadas onde especificamos um nome para a mesma e também parametros.

"""
# -*- coding: UTF-8 -*-
# Import
from collections import namedtuple

# Precisamos definir o nome e parametros.

# Forma 1
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

hulk = cachorro(idade=2, raca='pug', nome='Hulk')
print(hulk)

# Acessando os dados

# Forma 1:
print(hulk[0])  # Idade
print(hulk[1])  # Raça
print(hulk[2])  # Nome

# Forma 2:
print(hulk.idade)  # Idade
print(hulk.raca)  # Raça
print(hulk.nome)  # Nome

print(hulk.index('Hulk'))
print(hulk.count('Hulk'))
