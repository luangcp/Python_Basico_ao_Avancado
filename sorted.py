"""
Sorted

OBS: Não confunda, apesar do nome com a função sort() que ja estudamos em Listas
o sort() só funciona em listas. A utilização do sort na lista é ordenar

Podemos utilizaar o sorted() com qualquer iteravel

Como o proprio nome diz, sorted() serve pra ordenar.

OBS: O sorted, sempre retorna uma lista com os elementos do iteravel ordenados
"""

# Exemplos

numeros = [6, 2, 3, 1, 12, 55, 32, 11]
print(numeros)

print(sorted(numeros))
print(numeros)
"""
OBS: O sorted não modifica a lista original, ele cria uma nova, assim a lista original
permanece inalterada 

"""
print('\n')
numeros = [6, 2, 3, 1, 12, 55, 32, 11]
# Adicionando parametros ao sorted()

print(sorted(numeros, reverse=True))  # Ordena do maior para o menor
print('\n')

# Podemos utilizar o sorted para coisas mais complexas

usuarios = [
    {"username": 'Luan', "tweets": ['Eu amo futebol', 'Eu adoro pizzas']},
    {"username": 'Viviane', "tweets": ['Eu adoro bolos', 'Eu adoro maquiagem']},
    {"username": 'Hulk', "tweets": ['Eu amo uma comida']},
    {"username": 'franciscopeixe', "tweets": ['Eu amo nadar']},
    {"username": 'stelaAcoelha', "tweets": ['Eu adoro bolos', 'Eu adoro pizzas']},
    {"username": 'galaoDaMassa', "tweets": []},
    {"username": 'Bobuzinho', "tweets": [], "Cor": "preto"}

]

print(usuarios)
# Ordenando per username - Ordem alfabetica
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo numeros de tweets
print(sorted(usuarios, key=lambda usuario: usuario["tweets"]))

# Ultimo exemplo

musicas = [
    {"titulo": "Graveto", "Tocou": 8},
    {"titulo": "Largado as traças", "Tocou": 5},
    {"titulo": "Infiel", "Tocou": 7},
    {"titulo": "Gelo", "Tocou": 3},
    {"titulo": "Nocaute", "Tocou": 7}
]
# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['Tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['Tocou'], reverse=True))

