"""
Filter

filter() -> Filtrar dados de uma determinada coleção

# Filtrar dados apenas acima da media dos valores

valores = 1, 2, 3, 4, 5, 6

media = (sum(valores) / len(valores))

print(media)

"""
# -*- coding: UTF-8 -*-
# Biblioteca para trabalhar com dados estatisticos

import statistics

# Dados coletados de algum sensor
dados = [1.3, 1.7, 3.2, 4.55, 6.77, 9, 10.1, 0.5, -2, 3]
# Caculculando a media dos dados utilizando a função mean() - > significa media
media = statistics.mean(dados)
print(f'A media é {media}')

# OBS: assim como a função map(), a filter() recebe dois parametros, uma função e um iteravel

res = filter(lambda x: x > media, dados)
print(list(res))

# Basicamente uma mensagem autodestruida
print(f'Novamente: {list(res)}')  # Esse valor so fica na memoria na primeira utilização, então aq vai dar vazio
print('\n')

"""
OBS: Assim como na função map, após ser utilizados os dados de filter() 
eles são excluidos da memoria
"""

# Remoção de dados faltantes

paises = ['', 'Argentina', '', 'Brasil', 'Chile', 'Colombia', '', 'Venezuela']
print(paises)

# Pra remover esses em branco (faltantes)

res = filter(None, paises)
print(list(res))
print('\n')

# Outra forma

res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

# Outra forma
res = filter(lambda pais: pais != '', paises)
print(list(res))
print('\n')


"""
A diferença entre map() e filter() é:

map() -> recebe dois parametros, uma função e um iteravel e retorna um objeto
mapeando a função para cada elemento do iteravel

filter() -> Recebe dois parametros, uma função e um iteravel e retorna um objeto 
filtrando apenas os elementos de acordo com a função
"""

# Exemplo mais complexo:

# Dados para teste, exemplo twitter
# Username e twitts
usuarios = [
    {"username": 'Luan', "tweets": ['Eu amo futebol', 'Eu adoro pizzas']},
    {"username": 'Viviane', "tweets": ['Eu adoro bolos', 'Eu adoro maquiagem']},
    {"username": 'Hulk', "tweets": ['Eu amo uma comida']},
    {"username": 'franciscopeixe', "tweets": ['Eu amo nadar']},
    {"username": 'stelaAcoelha', "tweets": ['Eu adoro bolos', 'Eu adoro pizzas']},
    {"username": 'galaoDaMassa', "tweets": []},
    {"username": 'Bobuzinho', "tweets": []}

]
# A tarefa é filtrar os usuarios que estão inativos no twitter
# Alguem que não twittou nenhuma vez esta inativo no twitter

# abaixo diz: faça uma lista com o filtro: usuario: leia os twittis e os usuarios que tem 0 twitte faça uma lista
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos)

# Forma 2:
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)

# Uma lista vazia transformada em boolean é facil
print('\n')


# Combinar filter() e map()

nomes = ['Vanessa', 'Viviane', 'Liliane', 'Stela']

""" 
Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada 
nome tenha menos de 6 caracteres
"""

lista = list(map(lambda nome: f'Sua instrutora é: {nome}', filter(lambda nome: len(nome) < 6, nomes)))
print(lista)