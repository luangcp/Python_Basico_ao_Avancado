"""
Seek e Cursor

seek() -> é utilizada para movimentar o cursor pelo arquivo seek = procurar

cursor() ->
"""
# -*- coding: UTF-8 -*-

# Relembrando

arquivo = open('texto.txt', encoding='utf-8')

print(arquivo.read())

"""
A função seek() -> é utilizada para a movimentação do cursor pelo arquivo.
Ele recebe um parametro que indica onde queremos colocar o cursor
"""
# Movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(0)  # Voltou o cursor pra posição 0

print(arquivo.read())


arquivo.seek(20)  # Voltando pra posição 20 do texto
print(arquivo.read())

print('\n')
arquivo.seek(0)
# Função readline() -> Função que le o arquivo linha a linha

print(arquivo.readline())  # Le uma linha
# A classe é uma string, ou seja podemos usar todo comando de strings aqui

ret = arquivo.readline()
print(type(ret))
print(ret)
print(ret.split(' '))

print('\n')
# --------------------------------------------------------------------
# readlines()  -> le as linhas
arquivo.seek(0)
linhas = arquivo.readline()
print(len(linhas))  # Quantidade de linhas do arquivo

"""
OBS: Quando abrimos um arquivo com a função open, é criada uma conexão entre o arquivo
na disco do computador e o nosso programa. Essa conexão é chamada de streaming
Ao finalizar os trabalhos com o arquivo devemos fechar essa conexão. Para isso
utilizamos a função close()

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo
2- Trabalhar o arquivo;
3 - Fechar o arquivo;
"""

# 1 - Abrir o arquivo:
arquivo = open('teste.txt', encoding='utf-8')
# 2 - Trabalhar o arquivo:
print(arquivo.read())

print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado
# 3 - Fechar o arquivo
arquivo.close()
print(arquivo.closed)


