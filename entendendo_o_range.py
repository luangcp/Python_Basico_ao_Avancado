"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequencias numéricas, não de forma aleatória, mas sim de maneiras especificadaa.

Formas gerais:

range(valor_de_parada)

OBS: valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1)

# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: o valor de parada não inclusive (inicio especificado pelo usuario, e passo de 1 em 1 )

# Forma 3

range(valor_de_inicio,valor_de_parada,passo)

OBS: o valor de parada não inclusive (inicio especificado pelo usuario, e passo especificado pelo usuario )

# Forma 4 (inversa)

range(valor_inicio,valor_de_parada,passo)

OBS: o valor de parada não inclusive (inicio especificado pelo usuario, e passo especificado pelo usuario )

"""
# -*- coding: UTF-8 -*-
# Forma 1

for num in range(11):
    print(num)
print('\n')

# Forma 2

for num in range(4, 11):
    print(num)
print('\n')

# Forma 3

for num in range(4,11,2):  # Começa no 4, termina no 11 -1 e varia de 2 em 2
    print(num)
print('\n')

# Forma 4

for num in range(10,0,-1):  # Como se fosse uma contagem regressiva
    print(num)
print('\n')

# Obs: no terminal so funciona se fizer desse jeito:
lista = list(range(10))


