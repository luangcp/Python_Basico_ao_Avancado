"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas
Existem basicamente duas diferenças basicas:

1 - As tupla são representadas por parênteses (), (tambem é possivel fazer sem parenteses ex: 1, 2, 3, 4
2 - As tuplas são imutaveis, ao seu criar uma tupla ela não muda, toda
operação em uma tupla gera uma nova tupla

(4) -> Não é tupla
(4,) -> é tupla

"""
# -*- coding: UTF-8 -*-
print(type(()))  # Demostrando a classe da tupla

# Cuidado 1: As tuplas são representadas por () mas veja:
tupla1 = (1, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

# Abaixo TAMBÉM! é uma tupla
tupla2 = 1, 2, 3, 4, 5, 6, 7
print(tupla2)
print(type(tupla2))

tupla3 = (4)  # ISSO NÃO É IMA TUPLA
print(tupla3)
print(type(tupla3))

tupla4 = (4,)  # Isso é uma tupla
print(tupla4)
print(type(tupla4))

# CONCLUSÃO: Tuplas são definidas pela virgula e não pelo uso do parenteses

print('\n')
# Também é possivel gerar uma tupla dinamicamente com range(inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

print('\n')

# Desempacotamento de tupla
tupla4 = ('Luan', 'Pinheiro',)

escola, curso = tupla4
print(escola)
print(curso)

print('\n')
# Métodos para: adição, remoção de elementos nas tuplas não existen, sçao imutaveis!

# Soma*, Valor máximo*, malor minimo* e tamanho
# * Se os valores fore inteiros ou reais

tupla5 = 12, 34, 43, 129, 33, 14, 1, -4, 121

print(sum(tupla5))  # SOMA
print(max(tupla5))  # MAXIMO
print(min(tupla5))  # MINIMO
print(len(tupla5))  # TAMANHO DA TUPLA

print('\n')

# Concatenação de tuplas
# Concatenar é juntar

tupla6 = 1, 3, 5
tupla7 = 2,4, 6
print(tupla6 + tupla7)

print(tupla6)
print(tupla7)

# Lembre-se que tuplas são imutaveis, elas sozinhas não sofrem alteração

# Tupas são imutaveis mas podemos sobrescrever seus valores
print('\n')

# Verificar se determinado elemento esta contido na tupla

tupla8 = 1, 2, 3
print(3 in tupla8)

print('\n')

# Iterando sobre uma tupla:

tupla9 = 1, 23, 33, 44

for n in tupla9:  # pra cada numero dessa tupla imprime ele
    print(n)

for indice, valor in enumerate(tupla9):  # vai demonstrar indice 0 é isso indice 1 é aquilo
    print(indice, valor)
print('\n')

# Contando elementos dentro de uma tupla
tupla10 = 'a', 'b', 'c', 'a', 'b', 'd', 'f', 1, 2, 55
print(tupla10.count('c'))
print(tupla10.count(2))
print(tupla10.count('b'))


print('\n')

nome = tuple('Luan Gabriel Pinheiro')
print(nome)

print(nome.count('a'))

print('\n')

# Dicas na utilização de tuplas
"""
- Devemos utilizar tuplas SEMPRE que nao precisamos modificar os dados contidos em uma coleção

"""
# Exemplo 1 - Meses do ano, o ano tem 12 meses iguais, não faz sentido permitir a entrada de outro mes
meses = 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',\
        'Setembro', 'Outubro', 'Novembro', 'Dezembro'
print(meses)
# O acesso de elementos de uma tupla é semelhante a de uma lista
print(meses[5])  # Vai buscar o mes 5 da lista
print('\n')

# Iterar com while
i = 0
while i < len(meses):
    print(meses[i])
    i = i+1
print('\n')

# Verificamos em qual indice um elemento está na tupla
print(meses.index('Junho'))

# Caso o elemento não exista vai dar erro
# Assim como na lista o .index so informa o primeiro
print('\n')
# Slicing
# tupla[inicio:fim:passo]
print(meses[5:9:2])  # Começa no mes 5, vai até o 9, de 2 em 2

"""
Porque utilizar tuplas?
- Tuplas são mais rápidas do que listas.
- Tuplas deixam seu codigo mais seguro (são elementos imutaveis, nõa podem ser alterados)
"""

# Copiando uma tupla para outra
tupla11 = 1, 2, 3
print(tupla11)

nova = tupla11 # Na tupla não temos o problema de shallowcopy

print(nova)
print(tupla11)

outra = 4, 5, 6
outra = nova + outra
print(nova)
print(outra)
# ---------------------------------
