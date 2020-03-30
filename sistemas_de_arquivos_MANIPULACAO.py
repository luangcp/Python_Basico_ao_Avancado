"""
Sistemas de arquivo MANIPULAÇÃO

Como criar arquivos
como criar diretorios -> unicos, um a um

Primeiro passo é descobrir se um arquivo ou diretorio exisste

Documentação modulo os:
https://docs.python.org/3/library/os.html?highlight=os#module-os

"""
# -*- coding: UTF-8 -*-
# LEMBRAR DE USAR PARA ESCREVER EM ARQUIVOS -> encoding='utf-8'
import os

# Descobrindo se um arquivo ou diretorio existe
# Arquivo
print(os.path.exists('arquivo.txt'))  # False - não existe
print(os.path.exists('texto.txt'))  # True - Existe

# Diretorio : msm coisa
print(os.path.exists('Luan'))  # True
print(os.path.exists('arquivo'))  # False

# Saber se dentro do diretorio Luan existe o diretorio pacote_dentro_do_pacote
print(os.path.exists('Luan/pacote_dentro_do_pacote'))  #True

# Saber se dentro do diretorio Luan existe o diretorio pudim
print(os.path.exists('Luan/pudim'))  # False

# Saber se dentro do diretorio Luan/pacote_dentro_do_pacote existe luan4
print(os.path.exists('Luan/pacote_dentro_do_pacote/luan4.py'))

print('\n')
# CRIANDO ARQUIVOS

# Forma 1
open('arquivos-teste.txt', 'w', encoding='utf-8').close()

# Forma 2
open('arquivos-teste2.txt', 'a', encoding='utf-8').close()

# Forma 3
with open('arquivos-teste3.txt', 'w', encoding='utf-8') as arquivo:
    pass  # pass significa não faz nada, simplismente passa

# FORMA 4, MELHOR FORMA PRA SE FAZER ISSO
try:
    os.mknod('arquivo-teste4.txt')  # Comando os.mknod
except AttributeError:
    print('Ocorreu um erro')

# Se você estiver utilizando no mac OS, pode haver um erro de PermissionError

# OBS: Se criando um arquivo via mknod() se o arquivo ja existir teremos o erro FileExistsError

# PARA CRIAR DIRETORIOS
# Utilizar a função mkdir

try:
    os.mkdir('teste_criando_diretorio')
except FileExistsError:
    print('ERRO - Esse diretorio já foi criado')

print('\n')
# Também é possivel fazer acessando todos os caminhos (EXEMPLO LINUX)

# OBS: Se não tivemos permissão para criar um diretorio teremos um permission erros

# VENDO SE É POSSIVEL CRIAR UM DIRETORIO DENTRO DO OUTRO

try:
    os.mkdir('teste_criand_diretorio2/teste1/teste2')
except FileNotFoundError:
    print('ERRO -Não é possivel criar mais de um diretorio de uma vez! SÓ DA DIRETORIOS UNICOS')

print('\n')
# UMA MANEIRA DE SOLUCIONAR O PROBLEMA ACIMA É

try:
    os.mkdir('teste_criando_diretorio2')  # Um por um
    os.mkdir('teste_criando_diretorio2/Teste1')  # Um por um
    os.mkdir('teste_criando_diretorio2/Teste1/Teste2')  # Um por um
except FileExistsError:
    print('ERRO - Caso apareça erro é porque já foi criado, mude o nome do diretorio a ser criado')

print('\n')
# Outra maneira de fazer isso mais facil, da pra fazer com todos, USANDO makedirs

try:
    os.makedirs('teste_criando_deretorio3/Teste3/Teste4')
except FileExistsError:
    print('ERRO - Caso apareça erro é porque já foi criado, mude o nome do diretorio')

# OBS: Sempre lembrando que caso já exista algo com nome do diretorio vai dar o erro FileExistsErro

# Evitando o erro de pasta criada com msm nome sem precisar usar try e except
# USAR O , exist_ok=True

os.makedirs('teste_criando_deretorio3', exist_ok=True)  # Não vai dar erro, só vai executar sem criar nada

# COMO FAZER PARA RENOMEAR ARQUIVOS E DIRETORIOS
# Simples, utilizando o os.rename

# Mudando o nome de diretorios
try:
    os.rename('teste_criando_deretorio3', 'Renomeando_o_teste')
except FileExistsError:
    print('ERRO JÁ FOI RENOMEADO ESSE DIRETORIO')

# OBS, Se o diretorio não existir teremos um FileNotFoundError

# Obs: se o diretorio que queremos renomear não estiver vazio, teremos um OSError

# Mudar o nome de arquivos
# OBS IMPORTANTE, passar todo o caminho em ambos:
try:
    os.rename('teste_criando_diretorio/ola.txt', 'teste_criando_diretorio/novo.txt')
except FileExistsError and FileNotFoundError:
    print('ERRO')

print('\n')
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------

# DELETANDO ARQUIVOS **

# ** ATENÇÃO: Tome cuidado com os comandos de deleção.
# ** Ao deletarmos um arquivo de diretorio eles não vão para lixeira, eles somem

# Para remover ARQUIVOS utilizamos o os.remove
# removendo arquivos:

try:
    os.remove('para_ser_deletado.txt')
except FileNotFoundError:
    print('ERRO - O arquivo não existe, ou ja foi excluido, verifique o nome')

# OBS: No windows se vc for deletar um arquivo e ele estiver aberto ou em uso vai dar erro
# Caso o arquivo não exista teremos o FileNotFoundError

# OBS: Se voce informar um diretorio ao inves de um arquivo, teremos um IsAdirectoryError

# REMOVENDO DIRETORIOS VAZIOS:

try:
    os.rmdir('para_ser_excluido')
except FileNotFoundError:
    print('ERRO - O arquivo não existe, ou ja foi excluido, verifique o nome ')

# OBS: Se o diretorio tiver qualquer conteudo vai dar OSERROR
# Caso o diretorio não exista vai dar um FileNotFoundError

# Removendo diretorio com conteudos

"""
# ATENÇÃO NÃO DA CERTO, SÓ EXCLUI O QUE TEM DENTRO
try:
    for arquivo in os.scandir('teste_para_excluir'):
        if arquivo.is_file():
            os.remove(arquivo.path)
        if not arquivo.is_file():
            os.rmdir(arquivo.path)
except FileNotFoundError:
    print('Erro nome do arquivo inexistente ou já excluido, verificar')
"""
print('\n')

# -----------------------------------------------------------------
# -----------------------------------------------------------------

# Podemos resolver uma arvore de diretorios vazios
"""
os.removedirs('removendo_diretorios_com_diretorios/1')
"""

# OBS: Se alguns dos diretorios, contiver arquivos ou outro diretorios o processo para

"""
ATENÇÃO: Ao remover arquivos e diretorios com python eles não vão para lixeira
eles somem. PARA RESOLVER ISSO, baixar : pip install send2trash
"""

# Importando a biblioteca send2trash

from send2trash import send2trash

# ABAIXO NÃO VAI PRA LIXEIRA APENAS SOME
try:
    os.remove('exclui1.txt')  # Não vai para lixeira, simplismente some
except FileNotFoundError:
    print('ERRO - arquivo ja foi excluido, ou nome errad')

# ABAIXO VAI PRA LIXEIRA, UTILIZANDO send2trash (BIBLIOTECA)
try:
    send2trash('exclui2.txt')  # Vai para lixeira
except FileNotFoundError:
    print('ERRO - arquivo ja foi excluido e foi pra lixeira, ou nome errado')

# Se o arquivo não existir teremos OS ERRO

# Teste para ver se exclui diretorio para lixeira

try:
    send2trash('oioi')  # Vai para lixeira
except FileNotFoundError:
    print('ERRO - arquivo ja foi excluido e foi pra lixeira')

# send2trash envia arquivos e diretorios para a lixeira

# ----------------------------------------------------------------
# ----------------------------------------------------------------
print('\n')

# O codigo abaixo está COMENTADO MAS É MT IMPORTANTE, CRIANDO DIRETORIOS TEMPORARIOS
"""
# Trabalhando com arquivos/diretorios temporarios
# Utilizando os e tempfile

import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:  # Utilizado para criar o diretorio temporario
    print(f'Criei o arquivo temporario em {tmp}')  # Mostra o nome e o local do arquivo temporario
    with open(os.path.join(tmp, 'arquivos_temporarios.txt'), 'w', encoding='utf-8') as arquivo:  # Comando para escrever
        arquivo.write('Luan Pinheiro\n')  # Texto a ser escrito no arquivo temporario
    input()
"""

"""
Estamos criando um diretorio temporario abrindo o mesmo e dentro dele criando
um arquivo para escrevermos um texto, No final, usamos input() só para mantermos
os arquivos temporarios 'vivos' dentro dos blocos with.

OBS: Possivelmente o codigo pode não funcionar no windows 
"""

# Criando um ARQUIVO TEMPORARIO:
"""
import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    tmp.write(b'Luan Pinheiro\n')  # UTILIZANDO O b: convertendo para binario
    tmp.seek(0)
    print(tmp.read())


# OBS: O b utilizado é de binario, convertendo esse arquivo para binario
# Em arquivos temporarios só conseguimos escrever bits, pos isso utilizamos
# b como string

"""

