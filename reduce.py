"""
Reduce

OBS: A partir do python versão 3 e acima, a função reduce() não é mais uma função integrada
(built-in). Agora temos que importar e utilizar esta função a partir do modelo 'functools'

Guide van Rossum: Utilize a função reduce() se voce realmente precisa dela. Em todo caso,
99% das vezes um loop for é mais legivel

Para entender o reduce():

dados = [a1, a2, a3, ..., an]

def funcao(x, y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parametros: função e iteravel

reduce(funcao, dados)

A função reduce funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # Aplica a função nos dois promeiros elemnto da coleção e guarda o resultado
    Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo1 mais o 3° elemento, e guarda o res
    .
    .
    Passo n: resn = f(resn, an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado de
aplicação no anterior. No final, reduce() irá retornar o resultado final.

Alternativamente poderiamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2), a3), a4), ...) an)


"""
# Funcionamento na pratica
# Vamos utilizar a função reduce() para multiplicar todos os elementos de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 6, 7, 22, 33, 44, 55, 65, 32, 11, 2, 7]

# Para utilizar o reduce() nos precisamos de uma função que receba dois parametros
multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# Utlizando um loop normal

res = 1
for n in dados:
    res = res * n

print(res)