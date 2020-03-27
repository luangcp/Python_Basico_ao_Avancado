"""
Map -

Com Map, fazemos mapeamento de valores para a função.
"""

import math


def area(r):
    """ Calcula a área de um circulo com raio 'r'. """
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))
print('\n')
raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)
print('\n')

# Utilizando map

# Map é uma função que recebe dois parametros: O primeiro a função, o segundo um iteravel, Retorna um Map object

areas = map(area, raios)
print(areas)
print(type(areas))

print(list(areas))
print('\n')

# Forma 3 -  Map com Lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

"""
OBS: após utilizar a função map() depois da primeira utilização do resultado
ele zera.
É interessante pois limpa a memoria
"""
print('\n')

"""
Para fixar - Map
temos dados iteraveis:
dados: a1, a2, ... an
Temos uma função:
função: f(x)
Utilizamos a função map(f, dados) onde map ira 'mapear' cada elemento dos dados e aplicar a funçao

O map object: f(a1), f(a2), f(...), f(an)
"""

# Mais um exemplo: - CIDADES E TEMPERATURAS

cidades = [('Berlim', 29), ('Belo Horizonte', 30), ('Cairo', 22), ('Buenos Aires', 19), ('Los angeles', 26),
           ('Toquio', 26), ('Nova York', 19)]
print(cidades)
# Para mostrar em fahrenheit
# f = 9/5 * c + 32
# Lambda
# Dado na posição 0 é o nome, dado na posição 1 é a temperatura

c_para_f = lambda dado: {dado[0], (9/5) * dado[1] + 32}
print('Em fahrenheit:')
print(list(map(c_para_f, cidades)))


