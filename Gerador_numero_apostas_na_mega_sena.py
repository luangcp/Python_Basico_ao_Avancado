"""
Criando um gerador simples de apostas
# Autor: Luan Pinheiro
"""
# Importando a biblioteca random e a função randint
from random import randint

print('Bem-Vindo ao gerador de numeros de aposta')
aposta = int(input('Quanto numeros deseja apostar?'))

for i in range(aposta):  # Caso a aposta seja mais ou menos de 6 numeros mude
    print(randint(0, 90), end=', ')

