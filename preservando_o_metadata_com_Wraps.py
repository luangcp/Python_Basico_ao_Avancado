"""
Preservando o metadatas com Wraps

Metadatas -> são dados intrísecos em arquivos

Wraps -> são funções que envolvem elementos com diversas finalidades

exemplo: temos uma imagem e tal, os metadados dela seriam: largura, altura, tipo de imagem
tamanho da imagem em disco, ultima modificação.
"""

# Problema


def ver_log(funcao):
    def logar(*args, **kwargs):
        """Eu sou uma função dentro de outra"""
        print(f'Voce esta chamando: {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b


print(soma(10, 20))

# qual é o problema:
# A informação ta totalmente errada pois os metadados estão sendo alterados pelo decorator
print(soma.__name__)  # soma
print(soma.__doc__)  # soma dois numeros

# PARA RESOLVER

"""
Para resolver o problema
é necessario fazer o seguinte import
from functools import wraps
"""

from functools import wraps


def ver_log1(funcao):
    @wraps(funcao)  # SO COLOCAR ISSO AQUI E RESOLVE O PROBLEMA
    def logar(*args, **kwargs):
        """Eu sou uma função dentro de outra"""
        print(f'Voce esta chamando: {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log1
def soma1(a, b):
    """Soma dois números."""
    return a + b


print('\n')
print(soma1(10, 20))
print(soma1.__name__)  # soma
print(soma1.__doc__)  # soma dois numeros
