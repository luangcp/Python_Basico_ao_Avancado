"""
Trabalhando com JSON e Pickle

JSON -> JavaScript Object Notation  ( MUITO UTILIZADOS EM API'S DE EMPRESA, FACEBOOK, TWITTER, GOOGLE)

API -> São meios de comunicação entre os serviços oferecidos por empresas
(twitter, Facebook, Youtube..) e terceitos (nós desenvolvedores).

o JSON não trabalha com aspas simples apenas duplas, então o .dumps sempre concerta isso

Integrando o JSON com o Pickle:

instalar:  pip install jsonpickle
"""
import json
import jsonpickle
ret = json.dumps(['produto', {'Playstation 4': ('2TB', 'NOVO', 2200)}])

print(type(ret))
print(ret)


class Cachorro:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


hulk = Cachorro('Hulk', 'Pug')

print(hulk.__dict__)

ret = json.dumps(hulk.__dict__)

print(ret)

# JSON E Pickle  -> util para gravar um arquivo
print('\n')
ret = jsonpickle.encode(hulk)
print(ret)

# --------------------------------------------

# abrindo arquivo pra escrita

with open('hulk.json', 'w', encoding="utf8") as arquivo:
    ret = jsonpickle.encode(hulk)  # o encode modela o objeto pro formato jsonpickle
    arquivo.write(ret)
print('\n')
# recuperando a partir do json pra um objeto python
# lendo/fazendo a leitura

with open('hulk.json', 'r', encoding="utf8") as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)

