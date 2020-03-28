"""
PEP 8 - Python engancement Proposal

são propostas de melhorias para a linguagem python

The Zen of python

import this

A ideia da pep8 é que possamos escrever codigos do python de forma pythonica
forma bonita, agradavel visualmente

[1] - Utilize Camel case para nomes de classes;

class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minusulo, separados por underline para funções ou variaveis;
def Soma():
    pass


def soma_dois():
    pass

numero = 4


numero_impar = 5

[3] - Utilize 4 espaços para identação!!
certo:
if 'a' in 'banana':
    print('tem')

errado:
if 'a' in 'banana':
print('tem')

obs: não é recomendado usar o tab, usar 4 espaços é melhor    .

o python é totalmente dependente de identação

[4] - Linhas em branco:
- separar funções e definições de classes com duas linhas em branco
-Metodos dentro de uma classe devem ser separados com uma unica linha em branco

[5]- Imports:
-Imports devem ser sempre feitos em linhas separadas:

#Import errado:
import sys, os

#Importe certo:
import sys
import os

#Não há problemas em utilizar:
from types import StringType, ListType

#Caso tenha muitos imports de um mesmo pacote recomenda-se fazer:
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentarios ou docstrings e
antes de constantes ou variaveis globais.

[6] - Espaços em expressões e instruções:
# Não faça:
funcao( algo[ 1 ], { outro: 2 } )
dict ['chave'] = lista [indice]

x      = 1
y=2
variavel_longa=3

# Faça:
funcao(algo[1], {outro: 2})
dict['chave'] = lista[indice]

x=1
y=2
variavel_longa=3

[7] - Termine sempre uma instrução com uma nova linha
"""
# -*- coding: UTF-8 -*-
import this



