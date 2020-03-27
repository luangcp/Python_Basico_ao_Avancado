"""
Estruturas de repetição
Loop for

Loop -> é uma estrutura de repetição
for -> Uma dessas estruturas (para)

#Python
for item in interavel:
    //Esecução do loop

Utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis

Exemplos de iteraveis:
- String
 nome= 'Luan'
- List = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)
"""
nome = 'Luan'
lista = [1, 3, 4, 6, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

# Exemplo de for 1 (Iterando sobre uma string)
for letra in nome:
    print(letra)
print('\n')
# Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
"""
range(valor_inicial, valor_final)

Obs: o valor final não é incluso
ex: se for de 1 a 10 o 10 não vai 

outra forma de falar é que vai ate o valor final -1
"""
for numero in range(1, 10):
    print(numero)

# --------------------------------------------------
print('\n')

"""
Enumerate:
((0, 'L'), (1, 'u'), (2, 'a'), (3, 'n))
"""
for i, v in enumerate(nome):
    print(nome[i])
print('\n')
# Outro jeito:
for indice, letra in enumerate(nome):
    print(letra)
print('\n')

# Outro jeito:
for _, letra in enumerate(nome):
    print(letra)
print('\n')

# OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline(_)

for valor in enumerate(nome):
    print(valor[1])

# --------------------------------------------------
# Também pode ser usado assim
print('\n')
qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}° de {qtd} valores: '))
    soma = soma + num
print(f'A soma é {soma}')

# ----------------------------------------------------

nome = 'Atletico'
for letra in nome:
    print(letra)  # Como fazer pra imprimir td numa letra só??
    # É so fazer assim:
    print(letra, end='')


# Coisas legais:
# Tabela de emojis:
# https://apps.timwhitlock.info/emoji/tables/unicode
# Como usar:
# exemplo:
# Original : U+1F60B
# Modificado = U0001f60B
for x in range(3):
    for num in range(1, 11):
        print('\U0001f60B' * num)

# Outro emoji
# Original: U+1F60D
# Modificado:  U0001F60D
for x in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)
