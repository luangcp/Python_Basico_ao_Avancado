"""
Generatos - (tuple comprehensions)


"""
# Foi visto
nomes = {'Luan', 'Viviane', 'Kelly', 'Hulk', 'Francisco', 'Hulk', 'Stela'}
print(any([nome[0] == 'C' for nome in nomes]))

# Exemplos em Generators
# Só tirar as chaves
print(any(nome[0] == 'L' for nome in nomes))

# List Comprehension
res = [nome[0] == 'L' for nome in nomes]  # Tem colchetes
print(type(res))
print(res)
# Generator
res = (nome[0] == 'L' for nome in nomes)  # Tem parenteses
print(type(res))
print(res)
"""
OBS: Generator ocupa menos espaço em memoria
"""

# --------------------------------------------------------
# Importando biblioteca

# A utilidade de getsizeof -> Retorna a quantidade de bytes em memoria do elemento passado como parametro

from sys import getsizeof

# Mostra quantos bytes a string 'Luan' está ocupando em memoria. Quanto maior a string mais espaço ocupa
print(getsizeof('Luan'))

print(getsizeof('Pinheiro'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(999999999219))

print(getsizeof(True))

print('\n \n')

# ---------------------------------------------------------------------------

# Gerando uma lista de numeros com list comprehensions
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de numeros com set comprehensions
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de numeros com Dictionary comprehensions
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de numeros com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehensions: {list_comp} bytes')
print(f'Set Comprehensions: {set_comp} bytes')
print(f'Dict Comprehensions: {dict_comp} bytes')
print(f'Generator: {gen} bytes')


# Eu posso iterar no Generator Expression? SIM

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

# for num in gen:
# print(num)



