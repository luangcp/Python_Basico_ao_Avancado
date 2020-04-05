"""
Assertions (Checagens/Questionamentos)

Em python utilizamos a palavra reservada 'assert' para realizar simples
afirmações utilizadas nos testes.

Utilizamos o 'assert' em uma expressão que queremos checar se é valida ou não.
Se a expressão for verdadeira retorna None e caso seja false levanta um erro
do tivo AssertionError.

OBS: Nos podemos especificar, opcionalmente, um segundo argumente ou mesmo uma mensagem de erro
personalizada

Obs: a palavra asser pode ser utilizada em qualquer função ou codigo nosso. Não precisa
ser exclusivamene nos testes.

exemplo no terminal python:
assert 4==4 -> da ok

assert 4==2  -> da erro AssertionError

# ALERTA: Cuidado ao utilizar 'assert'
Se um programa python for executado com o parâmetro -O, nenhum assertion
será validado, Ou seja, todas suas validações ja eram

exemplo em terminal:

python -O Assertion_afirmacoes.py
(escreva uma coisa que não contem no exemplo e vai dar do msm jeito)
"""

# Exemplificando

def soma_num_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a+b


ret = soma_num_positivos(2, 4)
print(ret)

# ret2 = soma_num_positivos(-2, 4)  -> assertion erro
# print(ret2)


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'hamburguer',
        'doces',
        'batata frita',
        'cachorro quente'
    ], 'A comida precisa ser fastfood'
    return f'Eu estou comendo {comida}'


comida = input('Entre com o nome da comida: ')
print(comer_fast_food(comida))

# ALERTA: Cuidado ao utilizar 'assert'

