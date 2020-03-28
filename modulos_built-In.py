"""
Modulos Built-in -> Modulos que ja vem por padrão instalados na linguagem python

São modulos integrados que ja vem instalados no python.

Lista de modulos do python: https://docs.python.org/3/py-modindex.html

Tem que fazer o import deles pra não sobrecarregar a memoria, todos eles ja estão instalados
no python mas tem que ser importados
"""

# Utilizando alias (apelidos) para módulos/funções
import random as rdm  # o as serve pra dar um apelido pra modulos ou funções

print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando o *

from random import *

print(random())

# Importando todo o modulo

import random

print(random.random())

# Podemos também dar apelidos pra funçoes

from random import randint as rdi  # Dei o apelido pra função

print(rdi(5, 89))

# Fazendo varios imports, costumamos utilizar tuple para colocar multiplos imports de um msm modulo
# Muito usado pra python web, inteligencia artificial. Facilita a utilização
from random import (
    random,
    randint,
    shuffle,
    choice
)
print(random())

print(randint(3, 7))

lista = ['Luan', 'Pinheiro', 'Viviane']
print(shuffle(lista))
print(lista)

print(choice('Luan'))
