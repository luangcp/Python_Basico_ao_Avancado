"""
Listas aninhadas - [Nested Lists]

- Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays
    - Unidimecionais (Arrays/Vetores);
    - Multidimencionais (Matrizes):

* no python não existe arreys. Nos temos as listas

numeros = [1, 2, 3, 4, 5] em python lista | em C arrays

"""
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3

print(listas)
print(type(listas))

# Como fazemos para acessar os dados?
# Simples:

print(listas[0])  # Vai mostrar o elemento 0
print(listas[0], [1])  # Vai mostrar o elemento 0 e sua 2 posição

# Fazer acesso ao numero 8 do ultimo elemento
print(listas[2], [1])
print('\n')

# Iterando com loops em uma lista aninhada

for listas in listas:  # Para cada lista na minha lista de listas faça:
    for num in listas:
        print(num)

# List Comprehensions
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3
print('\n')
[[print(valor) for valor in lista] for lista in listas]

# Outros exemplos

# Gerando um tabuleiro/Matriz 3x3
print('\n')
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
print('\n')
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais
print('\n')

print([['*' for i in range(1, 4)] for j in range (1, 4)])
