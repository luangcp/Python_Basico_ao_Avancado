"""
Saíndo de loops com break

Funciona da mesma forma que nas linguagens C ou JAVA

Utilizamos o break para sair de loops de maneira projetada.

"""
# -*- coding: UTF-8 -*-

# Exemplo 1
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Sai do loop')

# Exemplo 2
while True:
    comando = input("Digite sair para sair: ")
    if comando == 'sair':
        break
