"""
Funções com parametro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se pensarmos em um programa qualquer, geralmente temos:
entrada -> processamento -> saída

Se pensarmos em uma função, já sabemos que temos funções que:
- Não possuem entrada
- Não possuem saída
- Possuem entrada mas não possuem saida
- Não possuem entrada mas possuem saída
- Possuem entrada e saída

"""
# -*- coding: UTF-8 -*-
# Refaturando uma função


def quadrado(numero):
    # return numero * numero
    return numero ** 2


print(quadrado(7))
print(quadrado(5))
print(quadrado(6))

# Se não colocar nenhum valor vai dar TypeError

# Outra:
# Refatorando a função


def cantar_parabens(aniversariante):
    print('Parabens pra voce')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o aniversariante!! {aniversariante}')


cantar_parabens('Luan')

# -----------------------------

"""
Funções podem ter n parametros de entrada. Ou seja, podemos reeber como entrada
em uma função quantos parametros forem necessarios. Eles são separados por virgula

"""

# Exemplo


def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print('\n')


print(soma(2, 5))
print(soma(1, 3))

print('\n')

print(multiplica(2, 2))
print(multiplica(22, 34))

print('\n')


print(outra(22, 3, 'oi'))  # soma esses dois primeiros numeros dps converte cada um em oi
print(outra(12, 12, 'LuanPinheiro'))  # soma esses dois primeiros numeros dps converte cada um em LuanPinheiro

# OBS: Se a gente informar o numero errado de parametro ou argumentos, teremos TypeError

# Nomeando parametros


def nome_completo(nome, sobrenome):
    return f'Seu nome comprelo é {nome} {sobrenome}'


print(nome_completo('Luan', 'Pinheiro'))

# A diferença entre parametros e argumentos

# Parametros são as variaveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função

# A ordem dos parametros importa!!

# Argumentos nomeados (Ketword argumentos)

"""
Caso utilizemos nomes dos parametros nos argumentos para informa-los, podemos
utilizar qualquer ordem
"""
# Nesse caso não importa a ordem pq está sendo especificado qual é qual
print(nome_completo(nome='Luan', sobrenome='Pinheiro'))
print(nome_completo(nome='Viviane', sobrenome= 'Betti'))

# Erro comum na utilização do return:
print('\n \n')


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num  # Total = numero de numeros na lista + numeros de numeros impares na lista
    return total  # O return deve estar exatamente onde o for finaliza, para que funcione corretamente


lista = [1, 2, 3, 4, 5, 6]
print(soma_impares(lista))