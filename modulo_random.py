"""
Modulo Random e o que são modulos?

- Em python, modulos nada mais são do que outros arquivos Python.

São uteis pra deixar os programas mais simples e reutilizar o codigo

Para utilizar os modulos temos que importa-los ou instala-los

Modulo Random -> Possui varias funções para geração de números pseudo-aleatorios

"""

# OBS: Existem duas formas de se utilizar um modulo ou função deste.

# Forma 1 - Importando todo o módulo (não recomendado)

import random  # Importando o modulo random

# Ao realizar o import de todo o modulo, todas as funções, atributos, classes e propriedades que estiverem
# Dentro do modulo ficarão disponiveis (ficarão em memoria). Caso vc
# Saiba quais funções vc precisa utilizar deste modulo, então esta
# Nao seria a forma ideal de utilização. USE A FORMA 2

print(random.random())

"""
Veja que para utilizar a função random(), nós colocamos o nome do pacote
e o nome da função, separadas por ponto.

OBS: Não confudaa função random() com o pacote random
função sempre tem parenteses()
A função randam() é apenas uma função dentro do modulo random
"""

# Forma 2 - Importando uma função especifica do modulo (recomendado)

from random import random  # Do modulo random importa pra mim a função random()

for i in range(10):
    print(random())  # 10 numeros aleatorios gerados

print('\n')
# Random é bastante utilizado em redes neurais ** (inteligencia artificial)

# Em alguns casos nao queremos numeros aleatorios entre 0 e 1
# Pra isso usamos a função uniform() -> Gerar entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7))  # 7 não é incluido

print('\n')
# Função randint() -> Gera valores entre os valores estabelecidos, somente inteiros

# Gerador de apostas para a mega sena

from random import randint

for i in range(6):
    print(randint(1, 90), end=', ')  # end= ', ' foi usado para colocar td na mesma linha

print('\n')

# Função choice() -> Mostra um valor aleatorio entre um iteravel

# importando
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))

# Se eu fizer assim ele escolhe uma letra por vez:
print(choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

print('\n')

# Função shuffle() -> Tem a funçãode embaralhar dados
# Importando
from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10']
print(cartas)
shuffle(cartas)  # Embaralhou
print(cartas)

# Caso queira embaralhar e dar uma carta ao usuario
print(cartas[0])