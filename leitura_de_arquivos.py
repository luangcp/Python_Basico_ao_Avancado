"""
Leitura de arquivos

Para ler o conteudo de um arquivo em python, utilizamos a função integrada open()
que literalmente significa abrir

open() -> Na forma mais simples de utilização, nós passamos apenas um parametro
de entrada, que neste caso é o nome do arquivo a ser lido. Essa função retorna
um _io.TextIOrapper e é com ele que trabalhamos então

documentação: http://docs.python.org/3/library/functions.html#open

# OBS: Por padrão a função open abre o arquivo para leitura, esse arquivo deve existir
ou então teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode r significa modo de leitura. r -> read() -> ler
"""

# Exemplo:

arquivo = open('texto.txt')
print(arquivo)
print(type(arquivo))
# Para ler o conteudo de um arquivo, após sua abertura, devemos utilizar a função read()
print(arquivo.read())

# OBS: A função read() lé todo o conteudo do arquivo.
# OBS: O python utiliza um recurso para trabalhar com arquivos chamado curso
# Esse cursor funciona como cursor quando estamos escrevendo

arquivo1 = open('teste.txt')
print(arquivo1)
print(type(arquivo1))

print(arquivo1.read())