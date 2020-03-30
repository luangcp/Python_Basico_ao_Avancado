"""
Funções de maior grandeza - Higher Order Functions - HDF

O que isso signica?

- Quando uma linguagem de programação suporte HDF, indica que podemos ter funções
que retornam outras funções como resultado ou mesmo que podemos passar funções
como argumentos para outras funções, e até mesmo criar variaveis do tipo de funões
nos nossos programas.

OBS: Na seção de funções, nos utilizamos isso

Em python as funções são cidadões de primeira classe, First class citizen
"""

# Exemplo utilizando funções de maior grandeza:


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as funções

print(calcular(4, 3, somar))

print(calcular(4, 3, diminuir))

print(calcular(4, 4, dividir))

print(calcular(4, 3, multiplicar))

print('\n')

# Nested Functions - Funções Aninhadas

"""
Em python podemos ter também funções dentro de funções, que são conhecidas
por Nested Functions, ou também Inner Functions (funções internas).
"""

# Exemplo Função para cumprimentar de acordo com o humor

from random import choice
# Lembrando que a função choice escolhe aleatoriamente uma coisa


def cumprimento(pessoa):
    def humor():  # Função interna (função dentro da função)
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa


# Testando

print(cumprimento('Luan'))

print(cumprimento('Viviane'))

# -----------------------------------------------------------

print('\n')

# Retornando funções de outras funções


def faz_me_rir():
    def rir():
        return choice(('hahahahahah', 'kkkkkkkkkkk', 'yayayayayayaay'))
    return rir


# Testando
rindo = faz_me_rir()
print(rindo())

print('\n')

"""
Inner Functions (funções internas / Nested Functions) podem acessar o escopo
de funções mais externas.
"""

from random import choice


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('HAHAHAHAHAH', 'KKKKKKKKKK', 'LOLOLOLOLOLO'))
        return f'{risada} {pessoa}'
    return dando_risada()


# Testando

rindo = faz_me_rir_novamente('Fernanda')


print(rindo)
print(rindo)
print(rindo)

