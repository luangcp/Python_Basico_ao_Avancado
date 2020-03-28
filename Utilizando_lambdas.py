"""
Utilizando Lambdas - Funções sem nome

Conhecidas pod expressões lambdas ou simplismente lambdas, são funções sem nome
ou seja, funções anonimas

# Função em python


def funcao(x):
    return 3 * x + 1


print(funcao(2))

# Exemplo de expressão lambda
lambda x: 3 * x +1

# Como utilizar a expressão lambda?

calc = lambda x: 3 * x + 1
print(calc(4))
print(calc(7))


"""
# -*- coding: UTF-8 -*-

# Podemos ter expressões lambdas com multiplas entradas
# função strip tira o espaço que não é necessario em uma string
# Função title torna a inicial da palavra maiusculo como deve ser
nome_completo = lambda nome, sobrenome: nome.strip().title() + '' + sobrenome.strip().title()

print(nome_completo('luan', ' PINHEIRO'))
print(nome_completo('LuAn    ', '   GaBrIeL'))

# Em funções python podem ter nenhuma ou varias entradas, em lambdas tbm

amar = lambda: 'Como não amar python'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x*y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x1 .... xn <expressão>

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# OBS: Se passar mais argumentos do que o experado vai dar typeError

print('\n')

# Outro exemplo

autores = ['Luan Pinheiro ', 'Viviane Betti ', 'Hulk k9', 'Francisco meu filho', 'Stela silvis',
           'kELLYS', 'Liliane O. Pinheiro']
print(autores)

# Ordenando essa lista pelo sobrenome
# Criando uma expressão nome, que verifique um por um olhando o sobrenome

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)
print('\n')

"""
Função quadratica:
f(x) = a * x **2 + b *x + c
"""

# Definindo a função


def geradora_funcao_quadratica(a, b, c):
    """ Retorna a função f(x) = a*x**2 + b * x * c """
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))
print('\n')

# Tbm pode fazer
print(geradora_funcao_quadratica(3, 0, 1)(2))


