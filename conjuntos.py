"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referencia à teoria dos conjuntos
da matematica

- Aqui no python, os conjuntos são chamados de Sets.

Dito isso, da mesma forma que na matematica:
 - Sets (conjuntos) não possuem valores duplicados;
 - Sets (conjuntos) não possuem valores ordenados;
 - Elementos não são acessados via indice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos, mas não nos importamos com a ordenação deles
quando não precisamos nos preoucpar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em python com chaves {}

Diferença entre conjuntos (sets) e Mapas (dicionarios)
    - Um dicionario tem chave/valor
    -um conjunto tem apenas valor

"""
# -*- coding: UTF-8 -*-

# Definindo um conjuntos

# Forma 1:
s = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}  # Tambem é possivel fazer com s = ({})
print(s)
print(type(s))
# Set não tem repetições
# Ele pode gerar um set de listas tuplas etc..
print('\n')

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

print('\n')

# --------------------------------------------------------------------------
# Importante lembrar que, além de não termos valores duplicados, não temos ordem
# Exemplificando

# Listas aceitam valores duplicados
lista = [99, 2, 34, 23, 12, 1, 44, 5, 5, 12, 2, 1]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados
tupla = (99, 2, 34, 23, 12, 1, 44, 5, 5, 12, 2, 1)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionarios não aceitam chaves duplicadas
dicionario = {}.fromkeys(lista, 'dict')
print(f'dicionario: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados
# Conjuntos não mantem a ordenação, ele faz uma ordenação propria
conjunto = {99, 2, 34, 23, 12, 1, 44, 5, 5, 12, 2, 1}
print(f'Conjuntos: {conjunto} com {len(conjunto)} elementos')

print('\n')

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s1 = {1, 'b', True, 34, 22, 44}
print(s1)
print(type(s1))

# Podemos iterar em um set normalmente:
for valor in s:
    print(valor)
print('\n')

# Usos interessantes com sets:
"""
Imagine que fizemos um formulario de cadastro de visitantes em um feira ou museu
e os visitantes informam manualmente a cidade de onde vieram.

Nos adicionamos cada cidade em uma lista python, ja que em uma lista podemos adicionar novos 
elementos e ter repetição.
"""

cidades = ['Belo Horizonte', 'São paulo', 'Campo grande', 'Cuiaba', 'Campo grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

""""
Agora precisamos saber quantas cidades distintas, ou seja, unicas temos.
O que vc faria? faria um loop na lista ...?
Podemos utilizar o set para isso!! :

"""
print(len(set(cidades)))  # O set remove duplicidades
print('\n')

# Adicionando elementos em um conjunto
s3 = {1, 2, 3}

s3.add(4)
s3.add(4)  # Duplicidade não gera erro, simplismente não é adicionado
print(s3)

print('\n')

# Removendo elementos do conjunto
s3.remove(3)  # Não é indice, informamos o valor a ser removido
# Nenhum valor é retornado
print(s3)
# OBS: caso o valor não seja encontrado será gerado o erro KeyError

# Forma 2:
s3.discard(2)
print(s3)
print('\n')

# Copiando um conjunto para outro
s4 = {1, 2, 3, 4}
print(s4)

# Forma 1 - Deep Copy - são independentes
novo = s4.copy()
print(novo)

novo.add(4)
print(novo)
print(s4)
print('Repare que adicionar um numero no NOVO, não adiciona nada no conjunto inicial')
print('\n')

# Forma 2 - Shallow Copy
novo = s4
novo.add(4)
print(novo)
print(s4)
print('Repare que adicionar um numero no NOVO, altera em ambos')
print('\n')

# Remover todos os itens do conjunto
s4.clear()
print(s4)
print('\n')

"""
Imagine que temos 2 conjuntos, um contendo estudandes do curso de Python e um 
contendo estudantes do curso de Java

"""
estudantes_python = {'Luan', 'Vivi', 'Hulk', 'Ellen', 'Liliane', 'Cleiton', 'Luci'}
estudantes_java = {'Fernando', 'Gustavo', 'Hulk', 'Alessandra', 'Gilmar', 'Luan'}
print(f'Estudantes de Python: {estudantes_python} \n Estudantes de Java: {estudantes_java}')
# Veja que alguns alunos que estudam python também estudam Java.
# Precisamos gerar um conjunto com nomes de estudantes unicos

# Forma 1 - Utilizando union (recurso matematico)
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)
print('\n')

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)
print('\n')

# REPARE, QUE OS NOMES QUE SÃO OS MESMOS, (QUE FIZERAM OS DOIS CURSOS) NÃO APARECEM NA LISTA UNICA

"""
GERAR UM CONJUNTO DE ESTUDANTES QUE ESTÃO EM AMBOS OS CURSOS:
"""
print('Gerando um conjunto com quem faz os dois cursos:')
# Forma 1 - Utilizando intersection:
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)
print('\n')

"""
GERAR UM CONJUNTO DE ESTUDANTES QUE NÃO ESTÃO EM OUTRO CURSO APENAS UM
"""
print('Estudantes que fazem só o python:')
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

print('Estudantes que fazem java')
so_java = estudantes_java.difference(estudantes_python)
print(so_java)
print('\n')

"""
Soma*, Valor maximo*, valor minimo*, tamanho
* Tem que ser inteiros ou reais
"""
s5 = {1, 2, 33, 56, 43, 123, 10, -3, 0}
print(s5)

print('Valor da soma de todos os numeros:')
print(sum(s5))
print('Valor maximo de todos os numeros:')
print(max(s5))
print('Valor minimo de todos os numeros:')
print(min(s5))
print('Valor do tamanho de todos os numeros:')
print(len(s5))