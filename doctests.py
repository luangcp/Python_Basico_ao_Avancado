"""
DocTests -> São testes que colocamos na docstrings das funções/metodos Python.

documentação escrita nas funções que funcionam como testes

TESTANDO NO TERMINAL -> python -m doctest -v doctests.py

Trying:
    soma(1, 2)  # um teste dentro da docstrig
Expecting:
    3
ok
1 items had no tests:
    doctests
1 items passed all tests:
   1 tests in doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.


OBS: Dentro do doctests o python não reconhece string com aspas duplas. Precisa ser aspas simples;
"""


def soma(a, b):

    """Soma os numeros a e v
     >>> soma(1, 2)  # um teste dentro da docstrig
     3

    >>> soma(4, 6)
    10
    """
    return a + b


# Outro exemplo aplicando o TDD


def duplicar(valores):
    """duplica os valores em um lista

    >>> duplicar([1, 2, 3, 4, 5])
    [2, 4, 6, 8, 10]

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([])
    []

    >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]


# Erro inesperado

def fala_oi():
    """fala oi

    >>> fala_oi()
    'oi'
    """
    return "oi"


# Um ultimo caso estranho

def verdade():
    """Retorna verdade

    >>> verdade()
    True
    """
    return True
