"""
Reversed

OBS: Não confunda com a função reverse() que estudamos nas listas e que serve
para colocar o reverso da lista

Já a função reversed funciona com qualquer iteravel, sua função é inverter o iteravel

A função reversed() retorna um iteravel chamado List Reverse iterator
"""

# Exemplos
lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(res)
print(type(res))

# Podemos converter o elemento retornado para uma lista, tupla ou conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Conjunto (set)
print(set(reversed(lista)))  # O set não se define ordem dos elementos

# Podemos iterar sobre o reversed
for letra in reversed('Luan Pinheiro'):
    print(letra, end= '')
print('\n')
# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Luan Pinheiro'))))

# Ja vimos como fazer isso mais facil com o slice de Strings
print('Luan Pinheiro' [::-1])

# Podemos tbm utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)

print('\n')
# Apesar que tambem ja vimos como fazer isso utilizando o proprio range
for n in range(9, -1, -1):
    print(n)

