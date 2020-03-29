"""
Montando um programa que receba uma lista de compras, e quando o usuario digitar sair ela crie um arquivo
com todas as compras em .txt

OBS:  OS ARQUIVOS DESSE PROGRAMA ESTÃO INDO PARA:  lista_de_compras.txt

OBS: A CADA VEZ QUE UMA NOVA LISTA FOR CRIADA A ANTIGA DESAPARECE
"""

# -*- coding: UTF-8 -*-

with open('lista_de_compras.txt', 'w', encoding='utf-8') as arquivo:
    nome = input('Escreva seu nome:')
    arquivo.write(f'Lista de compras de {nome}: \n')
    while True:
        compras = input('Informe sua lista de compras e quando acabar digite sair:')
        if compras != 'sair':
            arquivo.write(compras + '\n')
        else:
            break
