"""
stringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional
o software precisa ter permissão:
        - Permissão de leitura -> Para ler o arquivo.
        - Permissão de escrita -> Para escrever no arquino

StringIO -> Utilizado para ler e criar arquivos em memoria.
ele não vai gravar no disco vai ficar apenas na memoria

Para utilizar o stringIO primeiro fazemos o import
"""
# -*- coding: UTF-8 -*-
# Import
from io import StringIO

mensagem = 'Esta é apenas uma string normal'

# Podemos criar um arquivo em memoria ja com uma string inserida ou
# mesmo vazio para inserirmos texto depois
arquivo = StringIO(mensagem)

# Agora tendo o arquivo podemos utilizar tudo que ja sabemos
print(arquivo.read())

# Escrevendo outros textos
arquivo.write('Outro texto')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())