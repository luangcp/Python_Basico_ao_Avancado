"""
Funções com parametro padrão - Default paranters

- Funções onde a passagem de parametro seja opcional

ex: a função print, informar ou não um parametro na entrada é opcional
print('luan')
print()

ex: função que exige a entrada de parametros
def quadrado(numero):
    return numero ** 2

print(quadrado(2))


"""
# -*- coding: UTF-8 -*-
# Se eu colocar que um parametro ja recebe um valor ele se torna opcional


def exponencial(numero, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))
print(exponencial(3, 2))

print(exponencial(3))  # Por padrão eleva ao quadrada
print(exponencial(3, 5))  # Eleva a potencia informada pelo usuario
"""
OBS: se o usuario passar somente 1 argumento, este sera atribuido ao parametro numero
e sera calculado o quadrado desse numero;
Se o usuario passar 2 parametros, o promeiro sera atribuido ao parametro numero
e o segundo ao parametro potencia, então sera calculada esta potencia
"""
# ----------------------------------------------

# Obs: em funções python, os parametros com valores dafault (padrão) DEVEM sempre estar no final da declaração

# Outros exemplos:


def soma(num1=5, num2=3):
    return num1 + num2


print(soma(4, 3))
print(soma(4))
print(soma())
# ------------------------------------
print('\n')

# Exemplo mais complexo


def mostra_informacao(nome='Luan', instrutor=False):
    if nome == 'Luan' and instrutor:
        return 'Bem vindo instrutor Luan'
    elif nome == 'Luan':
        return "Eu pensei que você era o instrutor"
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao('Luan', True))

# Porque utilizar parametros com valor default?
"""
- Nos permite ser mais flexiveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legiveis de codigos;

"""

# Quais tipos de dados podemos utilizar como valores default para parâmetros?
"""
- Qualquer tipo de dado:
    - Numeros, strings, floats, Booleanos, Listas, tuplas, dicionarios, funções e etc;
"""

# Exemplos:
print('\n')


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))

print('\n')
# ---------------------------------------------------
# Escopo - evitar problemas e confusões...

# Variaveis globais
# Variaveis locais

instrutor = 'Luan'  # Variavel global


def diz_oi():
    instrutor = 'Python'  # Variavel local
    return f'Oi {instrutor}'


print(diz_oi())
# OBS: Se tivermos uma variavel local com o mesmo nome de uma variavel global, a local tera preferencia.
print('\n')

# ------------------------------


def diz_oi():
    prof = 'Luan'  # Variavel local
    return f'Olá {prof}'


print(diz_oi())
# print(prof)  # NameError, é uma variavel local é so funciona la dentro da função

# ---------------------------------------------

"""
total = 0


def incrementa():
    total = total + 1  # a variavel total não foi inicializada aqui dentro
    return total


print(incrementa())
"""
# Fazendo funcionar
print('\n')
total = 0


def incrementa():
    global total  # Avisando que queremos utilizar a variavel global

    total = total + 1  # a variavel total não foi inicializada aqui dentro
    return total


print(incrementa())
print(incrementa())
print(incrementa())

print('\n')

# --------------------------------------------
# Podemos ter funções que são declaradas dentro de funçoes, e tbm tem uma foma especial de escopo de variavel


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())
