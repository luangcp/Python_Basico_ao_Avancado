"""
Listas

Listas em python funcionam como vetores/matrizes (arrays) em outras linguagens,
com a diferença de serem DINAMICO e também podermos colocar QUALQUER tipo de dado.

Listas são mutaveis: podem ser mudadas constantemente

COMPARANDO:
lINGUAGEM C/JAVA: Arrays
 - Possuem tamanho e tipo de dados fixo;
    Ou seja, nessas linguagens se voce criar um array do tipo int e com tamanho 5, esse array
    sera sempre do tipo inteiro e podera ter sempre no maximo 5 valores

Já em PYTHON:
- Dinamico: Não possuem tamanho fixo, ou seja, podemos criar a lista e simplismente ir adicionando elementos;
- Qualquer tipo de dado: As listas não possuem tipo de dados fixo; ou seja, podemos colocar qualquer tipo de dado

As listas em python são representadas por colchetes: []

"""
# -*- coding: UTF-8 -*-
type([])  # Representa uma lista

lista1 = [1, 99, 33, 2, 5, 66, 12, 34, 56, 77, 81]

lista2 = ['g', 'h', 'j', 'a', 'U', 'y', 't']

lista3 = []

lista4 = list(range(11))

lista5 = list('Luan Pinheiro')

# Podemos facilmente checar se determinado valor está contido na lista
num = input('Entre com um número \n ')
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o numero {num}')

# Exemplo 2:
num = input('Entre com um número ou dado \n ')
if num in lista2:
    print(f'Encontrei o número ou dado {num}')
else:
    print(f'Não encontrei o numero ou dado {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o numero de ocorrencias de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionando elementos em listas
# Para adicionar elementos em listas, utilizamos a função append
# OBS: Com append, nós so conseguimos adicionar 1 elemento por vez

print(lista1)
lista1.append(42)
print(lista1)

# Tem como colocar uma lista dentro de outra lista
lista1.append([8, 3, 1])  # Coloca a lista como elemento único
print(lista1)

if [8,3,1] in lista1:
    print('Encontrei na lista')
else:
    print('Não encontrei na lista')

lista1.extend([123, 44, 67]) # Coloca cada elemento da lista como valor adicional á lista
print(lista1)

# ----------------------------------------------------------------------------------

# Podemos inserir um novo elemento na lista informando a posição do indice
# Isso não substitui o valor inicial, o mesmo sera deslocado pra direira da lista
lista1.insert(2, 'Novo valor')
print(lista1)


# Podemos facilmente juntar duas listas
lista6 = lista1 + lista2
print(lista6)

# Tambem da pra fazzer assim
# lista1.extend((lista2))

# Para imprimir a lista inversa:
# Podemos facilmente inverter os valores da lista utilizando o reverse
lista1.reverse()
lista2.reverse()

# Também é possivel com:
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Para ler a quantidade/tamanho dentro de uma lista
print(len(lista5))

# Podemos remover facilmente o ultimo elemento de uma lista
print(lista5)
lista5.pop()  # O comando .pop() remove o ultimo elemento
print(lista5)
# OBS: o pop tambem pode retormar o ulyimo elemento apagado

# Podemos remover um elemento pelo indice com o .pop()
# OBS: se não ouver nada no numero informado vai dar erro no index
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos com:
print(lista5)
lista5.clear()
print(lista5)

# Para repetir os elementos de uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista

# Exemplo 1
print('\n \n')
curso = 'Programação em python: Esssencial'
print(curso)
curso = curso.split()
print(curso)

# Exemplo 2
curso1 = 'Luan,gabriel,cardoso,pinheiro'
print(curso1)
curso1 = curso1.split(',')  # Especifica o separador de cada palavra
print(curso1)

print('\n \n')
# Convertendo uma lista em uma string
lista7 = ['programação', 'em', 'python:', 'Essencial']
print(lista7)

# Abaixo estamos falando: pega a lista7, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista7)
print(curso)

print('\n')
# Abaixo estamos falando: pega a lista7, coloca um cifrão entre cada elemento e transforma em uma string

curso = '$'.join(lista7)
print(curso)

print('\n')

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista8 = [1, 2.34, True, 'Luan', [1, 2, 3], 344332]
print(lista8)
print(type(lista8))

print('\n')

# Iterando sobre listas
# Exemplo 1 utilizando for:
lista9 = [1, 2, 3]
soma = 0
# Para cada elemento dentro da lista imprime esse elemento
for elemento in lista9:
    print(elemento)
    soma = soma + elemento
print(f'A soma dos elementos é {soma}')
print('\n')

# Exemplo 2 utilizando while:

carrinho = [] # O carrinho é uma lista
produto = ''  # O produto começa em branco e quando for colocado sair ele sai

while produto != 'sair':
    print('Adicione um produto na lista ou digite "sair" para sair: ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)  # Esse comando manda adicionar dados ao produto (.append())
for produto in carrinho:
    print(f' Os seus produtos são: {produto}')

print('\n')
# Listas com variaveis:
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

print('\n')

# Em lista fazemos acesso aos elementos de forma indexada
#         0         1        2         3
cores = ['verde', 'preto', 'branco', 'azul']
print(cores[0])  # Verde
print(cores[1])  # Preto
print(cores[2])  # Branco
print(cores[3])  # Azul

# Para ter acesso de forma indexada reversa

print(cores[-1])  # Azul
print(cores[-2])  # Branco
print(cores[-3])  # Preto
print(cores[-4])  # Verde

print('\n \n')
# Loops
for cor in cores:
    print(cor)
print('\n')
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos
lista10 = []
lista10.append(42)
lista10.append(33)
lista10.append(44)
lista10.append(44)
lista10.append(42)
lista10.append(33)
print(lista10)

# Outros metodos não tão importantes mas também uteis

# Encontrar o indice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual indice esta o valor 6?
print(numeros.index(6))

# Em qual indice esta o valor 9?
print(numeros.index(9))

# Caso não tenha o numero na lista sera apresentado erro: ValueError

print(numeros.index(5))  # Quando tem a repetição de valores ele so mostra o primeiro valor encotrado

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1)) # Buscando a partir do 1
print(numeros.index(5, 2)) # Buscando a partir do 2
# print(numeros.index(5, 4)) # Buscando a partir do 4 (vai dar erro pq n tem nenhum )

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6))  # Buscar o valor 8 entre 3 e 6

# Revisão de slicing

# lista(inicio:fim:passo)
# range(inicio:fim,passo)

# Trabalhando com slice de lista com o parãmetro 'incio'

lista11 = [1, 2, 3, 4]

print(lista11[1:])  # Iniciando no indice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parâmetro 'fim'

print(lista11[:2])  # Começa em 0, pega até o indice 2 -1

print(lista11[:2])  # Começa em 0, pega até o incide 4-1

print(lista11[1:3])  # Começa em 1, pega até o indice 3-1

# Trabalhando com slice de lista com parâmetro 'passo' (de 1 em 1, de 2 em 2)
print(lista11[1::2])  # Começa em 1 vai ate o final de 2 em 2
print(lista11[::2])  # Começa em 0 vai até o final de 2 em 2


# Invertendo valores em uma lista
nomes = ['Luan', 'Pinheiro']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

print('\n')

# É a mesma coisa que:
nomes.reverse()
print(nomes)
print('\n')

# Soma*, Valor Máximo*, Valor minimo*, Tamanho
# * somente com valores inteiros ou reais
lista12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 22, 43, 33, 22]


print(sum(lista12))  # Soma
print(max(lista12))  # Maximo
print(min(lista12))  # Minimo
print(len(lista12))  # Tamanho da lista

# Transforma uma listaem tupla
lista13 = [1, 2, 3, 4, 5, 6]
print(lista13)
print(type(lista13))

tupla = tuple(lista13)
print(tupla)
print(type(tupla))

# Desempacotamento de listas

lista14 = [1, 2, 3]
num1, num2, num3 = lista14
print(num1)
print(num2)
print(num3)

# OBS: se tivermos mais elementos para desempacotar do que variaveis teremos o erro: ValueError


# Copiando uma lista para outra (Shallow copy e Deep Coppy)

# Forma 1
lista15 = [1, 2, 3]
print(lista15)

nova = lista15.copy()

nova.append(4)
print(lista15)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas
# Ficaram totalmente independentes, ou seja, modificamos uma lista, não afeta a outra
# Isso em python é chamado de Deep copy (copia profunda)

# Forma 2 - Shallow copy
lista16 = [1, 2, 4]
print(lista16)

nova = lista16
print(nova)

nova.append(4)

print(lista16)
print(nova)

# Veja que utilizamos a copia via atribuição e copiamos os dados da lista para a nova lista, mas
# após realizar modificação em uma das listas, esse modificação se refletiu em ambas as listas.
# Isso em python é chamado de Shallow Copy.



