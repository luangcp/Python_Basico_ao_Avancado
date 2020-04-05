"""

PARA ESSA AULA TAMBÉM ESTÃO SENDO UTILIZADOS OS ARQUIVOS:
atividades.py
testes.py


Introdução ao modulo Unittest

Unittest -> Testes unitários

O que são testes unitarios?

Teste unitario é a forma de se testar unidades individuais de código fonte.

Unidades individuais podem ser: funções, métodos, classes, módulos etc.

OBS: Teste unitario não é especifico da linguagem Python.

Para criar nossos testes criamos classes que herdam de unittest.TestCase
e a partir de então ganhamos todos os 'assertions' presentes no módulo.

Para rodas os testes, utilizamos unittest.main()

TestCase -> Casos de testes para sua unidade

https://docs.python.org/3/library/unittest.html

# Conhecendo as assertions

Método                           Checa que
assertEqual(a, b)                a == b
assertNotEqual(a, b)             a != b
assertTrue(x)                    x é verdadeiro
assertFalse(x)                   x é falso
assertIs(a, b)                   a é b
assertIsNot(a, b)                a não é b
assertIfNone(x)                  x é none
assertIsNotNone(x)               x não é none
assertIn(a, b)                   a está em b
assertNotIn(a, b)                a não está em b
assertIsInstance(a, b)           a é instancia de b
assertNotIsInstancee(a, b)       a não é instancia de b


Por convenção, todos os testes em um test case, devem ter seu nome
iniciado com test_

Para executar os testes com unittest:

python nome_do_modulo.py

Paa executar testes com unittest no modo verbose:

python nome_do_modulo -v

# Docstrings nos testes

Podemos acrescentar e é recomendado, docstrings nos testes
"""

# Pratica - Utilizando a abordagem TDD
