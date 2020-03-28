"""
Funções com retorno ->

# Exemplificando retornos:

numeros = [1, 2, 3]

ret_pop = numeros.pop()  # A função pop exclui o ultimo numero
# O retorno de pop nesse caso é 3

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)  # A função print não retorna nada NONE
print(f'O retorno de print é: {ret_pr}')

OBS: Em python quando uma função n retorna nenhum valor vai ser impresso None

OBS: Funções python que retornam valores devem retornar esses valores com
a palavra reservada return

OBS: Nao precisamos necessariamente criar uma variavel para receber o retorno
de uma função. Podemos passar a execução da função para outras funções

OBS: Sobre a palavra reservada return
    1 - Ela finaliza a função, ou seja, ela sai da execução da função;
    2 - Podemos ter, em uma função, diferentes returns;
    3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores
"""
# -*- coding: UTF-8 -*-
# Exemplo função sem retorno


def quadrado_de_7():
    print(7*7)


ret = quadrado_de_7()

print(f'Retorno de 7 é {ret}')  # NÃO RETORNA NADA

# Exemplo refatorar a função para que ela retorne o valor


def quadrado_de_7():
    return 7*7


# Variavel criada para receber o retorno da função
ret = quadrado_de_7()

print(f'Retorno de 7 é {ret}')  # Agora ela tem o retorno graças ao return

# Daria na mesma fazer isso:
print(f'Retorno: {quadrado_de_7()}')

# Inclusive da pra fazer alteração ai
print(f'Retorno alterado: {quadrado_de_7()+1}')

print('\n \n')

# Refatorando a primeira função


def diz_oi():
    return 'oi '


alguem = 'Luan !'
print(diz_oi() + alguem)
# Quando o return é utilizado temos que utilizar o print pra aparecer
print('\n \n')

# -------------------- Exemplos --------------------
# Não pode executar nada depois do return


def diz_oi():
    print('Estou sendo executado antes do return')
    return 'oi '


# Exemplo 2 - Podemos tem em uma função diferentes returns:


def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())
print('\n \n')

# Exemplo 3 - Podemos em uma função retornar qualquer tipo de dado / multiplos valores


def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)
# Sabemos também que se quiser é so fazer
print(outra_funcao())  # IMPRIME COMO TUPLA
print(type(outra_funcao()))

print('\n \n')
# --------------------------------------------------------
# Vamos criar uma função para jogar a moeda
# Vamos usar bibliotecas

from random import random  # Importando do pacote random a função random


def joga_moeda():
    # Gera um numero pseudo-randomico entre 0 e 1 (pseudo- randomica pode ter repetição)
    # Numeros randomicos trazem a ideia de aletoriedade
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())

# TOP DEMAIS, gera numeros aleatorios, cada vez que executa da um numero diferente

# Erros comuns na utilização do retorno, que na verdade nem é erro mas codificação desnecessaria


def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    else:
        return False
    return


print(eh_impar())
# De cima é errado pq não tem a necessidade de colocar o ELSE
