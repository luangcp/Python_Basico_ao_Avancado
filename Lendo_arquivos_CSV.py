"""
Lendo arquivos CSV

comuns e ciencia de dados, anelises de dados, inteligencia artificial

CSV -> Comma Separeted Values - Valores separados por virgula

# Separador por virgula
1, 2, 3, 4, 5, 6, 7

"luan", "pinheiro", "pao", "hamburguer", "ciencia"

# Separador por ponto e virgula

1; 2; 3; 4; 5; 6; 7

"luan"; "pinheiro"; "pao"; "hamburguer"; "ciencia"

# Separador por espaço

1 2 3 4 5 6 7

"luan" "pinheiro" "pao" "hamburguer" "ciencia"

website onde conseguir dados:

http://dados.gov.br/dataset

OBS: LEMBRAR DE UTILIZAR O encoding="utf8"

A linguagem python possue duas formas diferentes de ler arquivos CSV:
    - Reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;


"""
import csv
# -*- coding: UTF-8 -*-

# Possivel de se trabalhar, mas não é o ideal, da trabalho.
with open('lutadores.csv', encoding="utf8") as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')[2:]
    print(dados)

print('\n')
# READER

from csv import reader

with open('lutadores.csv', encoding="utf8") as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # Pula o cabeçalho
    print(type(leitor_csv))
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)  {linha[1]}, e mede {linha[2]} centimetros')

# DictReader

from csv import DictReader

with open('lutadores.csv', encoding="utf8") as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']}")

# DictReader com outro separador, só usar o delimiter=' '

from csv import DictReader

with open('lutadores.csv', encoding="utf8") as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']}")