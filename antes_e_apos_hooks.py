"""
Unittest - Antes e após hooks

hooks -> são os testes em sí, ou seja, a execução do teste

e estamos falando aqui de executar algo antes e depois do testes

metodos:
setup() -> é executado antes de cada metodo de teste. é util para criarmos instancias
de objetos e outros dados;

tearDown() -> é executado ao final de cada método de teste. é util para excluir ou fechar
conexões com banco de dados

PARA ESSA AULA UTILIZAMOS robo.py e robo_testes
"""
import unittest


class ModuloTest(unittest):

    def setUp(self):
        # Configurações do setUp()
        pass

    def test_primeiro(self):
        # setup vai rodar antes do teste
        # tearDown vai rodar apos o teste
        pass

    def test_segundo(self):
        # setup vai rodar antes do teste
        # tearDown vai rodar apos o teste
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass


# UTILIZANDO robo.py e robo_testes.py