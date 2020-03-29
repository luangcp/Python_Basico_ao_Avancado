"""
Comando with

Também chamado de o bloco with
Passos para se trabalhar com arquivo:
# 1 - Abrimos o arquivo
# 2 - Manipulamos o arquivo
# 3- Fechamos o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos
utilizados sao fechados após o bloco with
"""
# -*- coding: UTF-8 -*-

# O bloco with
# Ele fecha o arquivo dps de executar
# É a forma pythonica de manipular arquivos
with open('texto.txt', encoding='utf-8') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)  # O arquivo está fechado? FALSO

print(arquivo.closed)  # O arquivo esta fechado? TRUE

