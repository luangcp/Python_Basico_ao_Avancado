"""
Tipo Float

tipo real,decima

casas decimais

* o separador de casas decimais na programação é o ponto e não virgula

3.5
2.4
2.11
1.100
1000.10


"""

# Errado do ponto de vista do float mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista float
valor1 = 3.5
print(valor1)
print(type(valor1))

# É possivel fazer dupla atribuição:
val1, val2 = 1, 44
print(val1)
print(type(val1))
print(val2)
print(type(val2))

# Podemos converter um float para um INT
"""
OBS: ao converter valores float para inteiro, nós perdemos precisão.
"""
res = int(val1)
print(res)
print(val1)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j
print(variavel)
print(type(variavel))