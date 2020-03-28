"""
Pacotes

Diferença entre modulo e pacote:

Modulo -> é apenas um arquivo python que pode ter diversas funções para utilizarmos

Pacote -> É um dicionario contendo uma coleções de modulo

OBS: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele
um arquivo chamado __init__.py

Nas versões do Python 3.x, não é mais obrigatoria a utilização desse arquivo
mas normalmente ainda é utilizado mara manter compatibilidade

"""

"""
Foi criado um pacote chamado Luan, dentro desse pacote já tinha um __init__ e foram
criados 2 pyhton files (luan1 e luan2). Dentro do pacote (Luan) foi criado um
novo pacote chamado (pacote_dentro_do_pacote) que tbm tinha um __init__ dentro
e foram criados mais dois python files (luan3 e luan4)

"""
from Luan import luan1, luan2  # Importando o pacote Luan

from Luan.pacote_dentro_do_pacote import luan3, luan4  # Importando o pacote dentro do pacote Luan

print(luan1.pi)  # Imprimindo a variavel pi que esta dentro de luan1 no pacote Luan

print(luan1.funcao1(4, 6))  # Imprimindo a função que esta dentro de luan1 no pacote Luan

print(luan2.curso)  # Imprimindo a variavel curso que esta dentro de luan2 no pacote Luan

print(luan2.funcao2())  # Imprimindo a função que esta dentro de luan2 no pacote Luan

print(luan3.funcao3())  # Imprimindo a função q esta dentro de luan3 no pacote_dentro_do_pacote. Q esta dentro de Luan

print(luan4.funcao4())  # Imprimindo a função q esta dentro de luan4 no pacote_dentro_do_pacote. Q esta dentro de Luan

# OBS: é possivel criar pacotes e postar la no Python.org pra que outras pessoas utilizem


# Também é possivel

from Luan.luan1 import funcao1  # Importar somente a função 1
from Luan.pacote_dentro_do_pacote.luan4 import funcao4  # Importar do pacote dentro do pacote dentro de luan 4 a função

print(funcao1(6, 9))



