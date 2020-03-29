"""
Modos de abertura de arquivos

r -> abre para leitura - padrão
w -> abre para escrita - sobrescreve caso o arquivo ja exista
x -> abre para escrita somente se o arquivo não existit
a -> abre pra escrita adicionando no final do arquivo caso exista
+ -> abre um arquivo para atualização, leitura e escrita. NUNCA SOZINHO,
o + sempre é usado junto a alguem, para leitura e escrita

http://docs.python.org/3/library/functions.html

"""
# -*- coding: UTF-8 -*-

# Usando o modo de abertura x, SÓ FUNCIONA SE NÃO EXISTIR O ARQUIVO
try:
    with open('Meu_cachorro_hulk', 'x', encoding= 'utf-8') as arquivo:
        arquivo.write('Meu cachorro chama hulk. \n')
except FileExistsError:
    print('Você ja criou um arquivo com esse nome, então deu o erro FileExistsError')
# Para sobrescrever usar a letra w


# Usando o modo de abertura a, que adiciona no final do texto
with open('frutas.txt', 'a', encoding= 'utf-8') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break

# OBS: O modo de abertura 'a' é bom para coisas que devem smp ser atualizadas
# Abrindo no formato A o arquivo SEMPRE será adicionado ao final do arquivo, não controlamos o cursor


# Exemplo usando mais +
# o mais inutil

with open('outro.txt', 'r+', encoding= 'utf-8') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair')
        if fruta != 'sair':
            arquivo.seek(0)
            arquivo.write(fruta + '\n')
        else:
            break