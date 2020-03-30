"""
Entendendo Iterators e Iteraveis  -> iterable retorna um iterators

Iterators ->
    - Um objeto que pode ser iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma
função next() é chamada;

Itarable ->
    - Um objeto que irá retornar um iterator quando a função iter() for chamada
    -


"""
nome = 'Luan'  # é um iterable mas não é um iterator.
numeros = [1, 2, 3, 4, 5, 6]  # é um iterable mas não é um iterator.

# print(next(nome)) -> não da pois não é um iterators

# mas podemos torna-lo iterators:

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))  # Da letra L
print(next(it1))  # Da letra u
print(next(it1))  # Da letra a
print(next(it1))  # Da letra n
print('\n')

print(next(it2))  # Da o numero 1
print(next(it2))  # Da o numero 2
print(next(it2))  # Da o numero 3
print(next(it2))  # Da o numero 4
print(next(it2))  # Da o numero 5
print(next(it2))  # Da o numero 6

# POR BAIXO DOS PANOS DO PYTHON
print('\n')
# O python faz o comando iter sozinho por baixo dos panos
for letra in nome:
    print(f'{letra}')
