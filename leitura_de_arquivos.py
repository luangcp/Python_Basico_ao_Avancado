"""
Leitura de arquivos

Para ler o conteudo de um arquivo em python, utilizamos a fun��o integrada open()
que literalmente significa abrir

open() -> Na forma mais simples de utiliza��o, n�s passamos apenas um parametro
de entrada, que neste caso � o nome do arquivo a ser lido. Essa fun��o retorna
um _io.TextIOrapper e � com ele que trabalhamos ent�o

documenta��o: http://docs.python.org/3/library/functions.html#open

# OBS: Por padr�o a fun��o open abre o arquivo para leitura, esse arquivo deve existir
ou ent�o teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode r significa modo de leitura. r -> read() -> ler
"""

# Exemplo:

arquivo = open('texto.txt')
print(arquivo)
print(type(arquivo))
# Para ler o conteudo de um arquivo, ap�s sua abertura, devemos utilizar a fun��o read()
print(arquivo.read())

# OBS: A fun��o read() l� todo o conteudo do arquivo.
# OBS: O python utiliza um recurso para trabalhar com arquivos chamado curso
# Esse cursor funciona como cursor quando estamos escrevendo

arquivo1 = open('teste.txt')
print(arquivo1)
print(type(arquivo1))

print(arquivo1.read())