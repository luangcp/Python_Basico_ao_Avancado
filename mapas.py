"""
Mapas -> Conhecidos em python como dicionarios

Dicionarios em python são representados por chaves {}
"""
# -*- coding: UTF-8 -*-
receita = {'jan': 100, 'fev': 250, 'mar': 300}
print(receita)


# Iterar sobre dicionarios:
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave}, recebi R$ {receita[chave]}')
print('\n')

# ------------------------------------------------------
# Acessando as chaves
print(receita)
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])
print('\n')

# Acessando os valores
print(receita.values())
for valor in receita.values():
    print(valor)
print('\n')

# Desempacotamento de dicionarios
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')
print('\n')

# Soma*,Valor Maximo*, Valor minimo*, tamanho
# * VALORES INTEIROS OU REAIS

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))