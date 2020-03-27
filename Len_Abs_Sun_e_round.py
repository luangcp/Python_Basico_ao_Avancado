"""
Len, Abs, Sum, Round

# Len:
len() - Retorna o tamanho (ou seja, o numero de itens) de um iteravel.

# Abs
abs() - Retorna o valor absoluto de um numero inteiro ou real. de forma basica,
seria o seu valor real sem o sinal -5 = 5 / 5 = 5 ( é como se fosse um modulo)
não se pode usar abs numa string

# Sum:
sum() - Recebe como parametro um iteravel, podendo receber um valor inicial,
e retorna a soma total dos elementos, incluindo o valor inicial

OBS: O valor inicial default é 0

# Round:
round() - retorna um numero arredondado para n digito de precisão após a casa
decimal. Se a precisão não for informada retorna o inteiro mais proximo da entrada

"""
# So pra revisar

# Função LEN
print(len('Luan Pinheiro'))

print(len((1, 2, 3, 4, 5)))

print(len([1, 2, 3, 4, 5]))

print(len({1, 2, 3, 4, 5}))

print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

print(len(range(0, 10)))

print('\n')
# Por dentro dos panos, quando utilizamos a função len() o python faz o seguinte:
# Toda a função que começa e termina com 2 underlines é chamada de dunder
# Dunderlen:
print('Luan Pinheiro'.__len__())

# -------------------------------------------------------------------

# Exemplos Abs():

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))
# Nao se pode fazer abs com strings

# ------------------------------------------------------------------

# Função sun()
print(sum([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5], 5)) # Passando como valor inicial o 5. Ent vai ser 15+5 =20

print(sum([1.33, 1.44, 2.33, 5]))

print(sum((1, 2, 3, 4, 5)))

print(sum({1, 2, 3, 4, 5}))

print(sum({'a': 1, 'b': 2, 'c': 3}.values()))  # colocar sempre o .values pra somar so os valores


# Função round:

# Exemplos

print(round(10, 2))
print((round(10.5)))
print(round(10.2))
print(round(10.6))
print(round(1.2129999, 2))
print(round(1.2121212121, 2))






