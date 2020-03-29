"""
Sistemas de arquivos NAVEGAÇÃO

Computadores celulares e tablets armazenam conteudos em arquivos
Os arquivos ficam dentro de diretorios -> formando contaudos

Esses arquivos armazenados podem ser documentos, fotos, videos, dados,
qualquer tipo de arquivo

Os arquivos possuem duas partes seu_nome.extensão
ex:  texto.txt
     arquivo.pdf
     imagem.jpg  ou imagem.png
     programa.py

metadados: são as coisas que o computador entende, como tamanho da imagem
tipo de imagem, nome da imagem, ultima modificação

Os arquivos são organizados em diretorios também chamados de pastas

Os diretorios são organizados de forma hierarquica , diretorio dentro de diretorio etc

Diretorio raiz: é o diretorio principal


                            -------> PASTA 4
                            I                             I
                            I
                ----> PASTA 2
                I
                I
EXEMPLO:  PASTA RAIZ                               E assim por diante
                I
                I
                ----> PASTA 3
                            I
                            I
                            ------> PASTA 5


Diferenças entre sistemas operacionais Windowns C:/ e POSIX /

Windows C:/ : comuns, o seu diretorio raiz é o C:

POSIX / :  Sistemas operacionais modernos, ex: MAC OS e LINUX, o seu
diretorio raiz é o /

Path: caminho do arquivo até o diretorio onde elé esta armazenado.
também conhecido como endereço  ex: c:/Usuarios/Luan/Blablabla..
                                    /home/luan/teste.py

a principal diferença entre windows e posix é a barra

Paths absoluto: Pega tudo da raiz ate o arquivo

Paths relativo: ex: /home/workspaces/backups/.../  esses ... deixam de forma relativa
o ../ volta um diretorio
por isso quando usamos o cd .. ele retorna pro anterior

É IMPORTANTE CONHECER AS ESTRUTURAS DE ARQUIVOS DO WINDOWS DO LINUX E DO MAC


----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos
importar e fazer uso do modulo os.

os -> Operating System - Sistema opefarional
"""
# -*- coding: UTF-8 -*-
# Fazer import
import os

# getcwd() -> pega o current work directoy
# RETORNA O CAMINHO ABSOLUTO
print(os.getcwd())  # C:\Users\luang\PycharmProjects\guppe

# Para mudar o diretorio, podemos utilizar o chdir()

os.chdir('..')  # C:\Users\luang\PycharmProjects
print(os.getcwd())

os.chdir('..')  # C:\Users\luang
print(os.getcwd())

os.chdir('..')  # C:\Users
print(os.getcwd())

os.chdir('..')  # CHEGOU NA RAIZ
print(os.getcwd())


# começando da raiz
# CHECANDO SE UM DIRETORIO É ABSOLUTO OU RELATIVO LINUX E MAC
# print(os.path.isabs('/home/luang/'))



"""
OBS para usuario Windows
Se você estiver utilizando um computador com windows
tera que ter cuidado ao verificar diretorios.
"""
# No windows
# lembrar de no windows usar \\ ao inves de barra invertida
print(os.path.isabs('C:\\Users\\luang'))

# POIS NAO SE PODE USAR O BARRA INVERTIDA NO PYTHON

# Podemos identificar o sistema operacional com o módulo os
print(os.name)  # Posix (Linux e Mac), nt (Windows)

# Podemos ainda ter mais detalhes do sistema operacional
# print(os.uname()) # no linus e no mac OS

import sys

print(sys.platform)  # Mostrando a plataforma que está sendo utilizada

print(os.getcwd())

res = os.path.join(os.getcwd())

os.chdir(res)

print(os.getcwd())

# Vejja que o os.path.join() recebe dois parametros
# sendo o primeiro o diretorio atual e o segundo o diretorio
# que sera juntado ao atual

# Podemos listar os diretorios e arquivos com o listdir()

print(os.listdir('C://'))  # No linux usar /etc
print(len(os.listdir('C://')))  # Vendo quantos arquivos tem

# Podemos listar os arquivos e diretorios com mais detalhes com scandir()
scanner = os.scandir('C://')

arquivos = list(scanner)
print(arquivos)
print(dir(arquivos[0]))
print(arquivos[0].name)


# OBS: Quando utilizamos a função scandir() nos precisamos fechalas
scanner.close()
