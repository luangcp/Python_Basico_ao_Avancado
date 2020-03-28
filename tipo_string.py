"""
O tipo string

Em python um dado é considerado do tipo string sempre que:
-estiver entre aspas simples -> 'uma string', '234' 'a'
-Sempre que estiver entre aspas duplas -> "oi" "234" "a"
-Sempre que estiver entre aspas simples triplas -> '''oi''' '''234''' '''a'''
-Sempre que estiver entre aspas simples triplas ->


"""
# -*- coding: UTF-8 -*-
nome = 'Luan Pinheiro'
print(nome)
print(type(nome))

nome = "Luan Pinheiro"
print(nome)
print(type(nome))

nome = '''Luan Pinheiro'''
print(nome)
print(type(nome))

nome = """Luan Pinheiro"""
print(nome)
print(type(nome))

# o \n na programação serve pra pular uma linha
nome = '\n Luan \n Gabriel \n Cardoso \n Pinheiro'
print(nome)
print(type(nome))


# ----------------------------------------------------

nome = 'Hulk e Francisco'
print(nome.upper())

nome = 'Hulk e Francisco'
print(nome.split())  # Transforma em uma lista de string

# [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# [ 'H', 'u', 'l', 'k', ' ', 'F', 'r', 'a', 'n', 'c', 'i', 's', 'c', 'o']

print(nome[0:4])  # Slice de string

print(nome[5:14])  # Slice de string

"""
[::-1] -> Comece do primeiro elemento, vá ate o ultimo elemento e inverta
"""

print(nome[::-1])  # Comando pra inverter a string

print(nome.replace('H', 'P'))  # Comando para substituir uma letra por outra

