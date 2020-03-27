"""
Loop While

while = enquanto

while expressão_booleana:
    //execução do lupe

O bloco do while será repetido enquanto a expressão booleanna for verdadeira.

Expressão booleana é toda aquela expressão onde o resultado é verdadeiro ou falso.

exemplo:
num = 5
num<5

"""
# Exemplo 1

num = int(input('Entre com um numero'))

while num < 10:
    print(num)
    num = num + 1  # Se não tiver isso vai dar loop infinito
# OBS: Em um loop while, é importante que cuidemos do criterio de parada.

# Exemplo 2:

resposta = ''
while resposta != 'sim':
    resposta = input('Ja acabou jessica?')
