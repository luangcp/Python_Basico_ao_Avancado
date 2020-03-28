"""
Modulos collections - Counter -> Contador

https://docs.python.org/3/library/collections.html#collections.Counter

Collections é Conhecido por -> High-Perfomance Container Datatypes
alta perfomace

Counter -> recebe um iteravel como parametro e cria um objeto do tipo Collections Counter
que é parecido com um dicionario, contendo como chave o elemento da lista passada como
parametro e como valor a quantidade de ocorrencias desse elemento
"""
# -*- coding: UTF-8 -*-
# Utilizando o Counter
# Primeiro tem que importar o counter (importando uma biblioteca)

from collections import Counter  # Biblioteca importada (aprender dps)

# Podemos utilizar qualquer iteravel, aqui usamos uma lista
lista = [1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 99, 0, 100, 11, 23, 14, 15, 16, 17, 31, 22, 34, 44, 55, 65, 31, 12]

# Utilizando o counter
res = Counter(lista)

print(type(res))
print(res)
# ELE CONTA QUANTAS VEZES CADA COISA APARECEU, NU MT UTIL

"""
Veja que para cada elemento da lista o Counter criou uma chave e colocou como valor a quantidade 
de ocorrencias.
"""
# Exemplo 2:
print(Counter('Luan Gabriel Cardoso Pinheiro'))  # Mostra quantas vezes cada letra vai aparecer, inclusive o espaço
print('\n')
print('\n')
# Exemplo 3:

texto = """ O Clube Atlético Mineiro (conhecido apenas por Atlético e cujo acrônimo é CAM) é um clube brasileiro de
futebol sediado na cidade de Belo Horizonte, Minas Gerais.[3] Fundado em 25 de março de 1908 por um grupo de
estudantes, tem como suas cores tradicionais o preto e o branco. Contudo, o clube teve como primeiro nome Athlético
Mineiro Football Club .[4] Seu símbolo e alcunha mais popular é o Galo, mascote oficial no final da década de 1930.
O Atlético é um dos maiores e mais populares clubes de futebol do Brasil .

Embora tenha atuado em outras modalidades esportivas ao longo dos anos, seu reconhecimento e suas principais conquistas
foram alcançados no futebol. O clube é o maior campeão do Estado de Minas Gerais, com 44 títulos do Campeonato Mineiro
além de ser o maior vencedor do Clássico Mineiro,[9] com uma grande vantagem contra seu rival, o Cruzeiro. A nível
nacional, foi campeão brasileiro uma vez, em 1971, e conquistou outros três títulos nacionais oficiais: a Copa dos 
Campeões (FBF) em 1937, a Copa dos Campeões (CBD) em 1978, e a Copa do Brasil, em 2014.[19] Na esfera internacional,
possui quatro títulos oficiais:[20] uma Copa Libertadores da América,[21] duas Copas Conmebol [nota 1][27] e uma
Recopa Sul-Americana.[28] Um outro grande feito do Atlético é o de ser, junto ao Dublin-URU, Santa Cruz, Arsenal-ING,
e do Flamengo, um dos 5 únicos clubes do mundo que já venceram a Seleção Brasileira de Futebol[29] """

palavras = texto.split()
res = Counter(palavras)
print(res)
# Mostra quantas vezes cada palavra do texto apareceu! Incrivel

# Descobrir as 5 palavras mais utilizadas no texto
print(res.most_common(5))
