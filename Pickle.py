"""
Pickle

Com o pickle salvamos os dados de forma serializada, ou seja, são salvos no formato binario, hexadecimal

A função do pickel é realizar o seguinte processo:

Objeto Python -> Binarilazação

Binarização -> Objetos Python

Este processo é chamado de serialização/deserialização

OBS: O módulo Pickle não é seguro contra dados maliciosos e desta forma não é
recomendado trablahar com arquivos pickle vindos de outras pessoas
que voce nao conheça ou de fontes desconhecidas

OBS: LEMBRAR DE UTILIZAR O encoding="utf8"
"""
import pickle
# -*- coding: UTF-8 -*-


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f'{self.__nome} esta comento ...')

    @property
    def nome(self):
        return self.__nome


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} esta miando')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} esta latindo')


felix = Gato('Felix')
hulk = Cachorro('Hulk')


# wb é de escrita binario
# nao vamos conseguir vizualizar porra nenhuma, pq ta em binario, serializado, transformados e hexadecimal ppra ngm ler
with open("animais.pickle", 'wb') as arquivo:
    pickle.dump((felix, hulk), arquivo)  # Dump recebe dois parametros o que vai receber e o arquivo


# FAZER A LEITURA DE ARQUIVOS PICKLE

with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)  # carrega o arquivo e descompacta 
    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')

    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do cachorro é {type(cachorro)}')

