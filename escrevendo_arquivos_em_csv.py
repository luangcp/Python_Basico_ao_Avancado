"""
Escrevendo em arquivos CSV

reader()  (leitor), writer() (escritor)

o metodo writer() cria um objeto que nos permite escrever em arquivos csv

writerow() ->  Escreve uma linha, esse metodo recebe uma lista


r -> abre para leitura - padrão
w -> abre para escrita - sobrescreve caso o arquivo ja exista
x -> abre para escrita somente se o arquivo não existit
a -> abre pra escrita adicionando no final do arquivo caso exista
+ -> abre um arquivo para atualização, leitura e escrita. NUNCA SOZINHO,
o + sempre é usado junto a alguem, para leitura e escrita


OBS: LEMBRAR DE UTILIZAR O encoding="utf8"
"""
import csv
# -*- coding: UTF-8 -*-

from csv import writer

# MUITO TOP, Criou a lista filmes e ainda separou por cores cada coisa

with open('filmes.csv', 'w', encoding="utf8" ) as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Genero', 'Duracao'])  # cabeçalho
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o Genero: ')
            duracao = input('Informe a duracao em minutos: ')
            escritor_csv.writerow([filme, genero, duracao])


# DictWriter

from csv import DictWriter

with open('filmes2.csv', 'w', encoding="utf8") as arquivo:
    cabecalho = ['Titulo', 'Genero', 'Duracao']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o Genero: ')
            duracao = input('Informe a duracao em minutos: ')
            escritor_csv.writerow({"Titulo": filme, "Genero": genero, "Duracao": duracao})

