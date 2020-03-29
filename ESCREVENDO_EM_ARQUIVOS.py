"""
Escrevendo em arquivos

independente de ler ou escrever o primeiro passo é abrir
então em escrevendo arquivos tbm utilizamos open()

OBS: Ao abrir um arquivo para leitura não podemos realizar escrita nele. Apenas ler
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lé-lo, somente
escrever nele

# Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write
Esta função recebe uma string como parametro, caso contrario teremos type error

Abrindo um arquivo para escrita com o modo w, se o arquivo n existir será criado
caso já exista, o anterior sera apagado e um novo será criado. Dessa forma,
todo o conteudo no arquivo anterior é perdido
"""
# -*- coding: UTF-8 -*-
# Exemplo de esrita, modo 'w' . write (escritaa)
with open('texto.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Escrever dados em arquivos é mt facil. \n')
    arquivo.write('Podemos colocar quantas linhas quisermos. \n')
    arquivo.write('Essa é a ultima linha.')


# Forma tradicional/não paythonica:
arquivo = open('Aula_escrevendo_arquivos.txt', 'w', encoding='utf-8')

arquivo.write('Esse arquivo foi criado através da aula "escrevendo'
              'em arquivos \n')
arquivo.write('Lembre-se sempre de utilizar : # -*- coding: UTF-8 -*-  \n')
arquivo.write('Além disso, na linha de abertura usas, encoding="utf-8" ')

with open('luan.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Luan' * 100)

# Exemplo usando while

with open('frutas.txt', 'w', encoding='utf-8') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair:')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break
