"""
Modulo collections: Ordered Dict

# Em um diionario a ordem de inserção dos elementos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3 , 'd': 4}

for chave, valor in dicionario.items():
    print(f'chave = {chave}: valor = {valor}')


"""
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3 , 'd': 4})

for chave, valor in dicionario.items():
    print(f'Chave = {chave}: Valor = {valor}')

# Entendendo a diferança entre dict e ordered dict
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 2, 'b': 1}

print(dict1 == dict2)  # True pois a ordem não importa nos dicionarios

# Ordered dict
odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'a': 2, 'b': 1})

print(odict1 == odict2)  # False pois a ordem importa