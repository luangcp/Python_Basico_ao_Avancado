"""
Carrinho de compras:
    Produto 1:
        - Nome
        - Quantidade
        -Preço
    Produto 2:
        - Nome
        - Quantidade
        - Preço

Poderiamos utilizar uma lista para isso? SIM
"""
# 1- Poderiamos utilizar uma lista para isso? SIM

carrinho = []

produto1 = ['Playstation 4', 1, 2000]
produto2 = ['Bola de futebol', 1, 70.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
print('\n')

# Teriamos que saber qual é o indice de cada informação no produto

# Forma 2 - Poderiamos usar um tupla para isso? SIM
produto1 = ('Playstation 4', 1, 2000)
produto2 = ('Bola de futebol', 1, 70.00)

carrinho = (produto1, produto2)
print(carrinho)
# Teriamos que saber qual é o indice de cada informação no produto
print('\n')

# Poderiamos utilizar um dicionario para isso? SIM
carrinho = []
produto1 = {'nome': 'Playstation 4', 'Quantidade': 1, 'Preço': 2000}
produto2 = {'nome': 'Bola', 'Quantidade': 1, 'Preço': 75.50}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
# Dessa forma facilmente add ou removemos produtos no carrinho, e em cada produto
# Podemos ter certeza sobre cada informação

print('\n')
