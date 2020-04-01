"""
Programação Orientada a Objetos - Classes

Em POO, Classes nada mais são do que modelos dos objetos do mundo real
sendo representados computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle
das lampadas da sua casa.

nesse caso temos um objeto do mundo real = lampada
então criamos uma classe chamada lampada, tendo assim um tipo de dado
chamado lampada

Classes podem conter:
    - Atributos -> Representão as caracteristicas do objeto. Ou seja,
pelos atributos conseguimos representar computacionalmente os estados de
um objeto. No caso da lampada, possivelmente iriamos querer saber se a lampada
é 110 ou 220 volts, se ela é branca amarela, vermelha ou outra cor, qual é a
luminosidade dela e etc..

    - Metodos (funções) -> Representam os comportamentos do objeto, ou seja, as
ações que esse objeto podem fazer no seu sistema. No caso da lampada, por exemplo
um comportamento comum que muito provavelmente iriamos querer representar no nosso sistema
é o de ligar e desligar a mesma.

Em python para definir uma classe, utilizamos a palavra reservada class

OBS: Utilizamos a palavra 'pass' em python, quando temos um bloco de codigo
que ainda não está imprementado.

OBS: Quando nomeamos uma classe em python, utilizamos por convenção o nome com
inicial em maiusculo. Se o nome for composto utilizamos as iniciais de ambas as
palavras em maiusculo, todas juntas.

DICA: Em computação não utilizamos pontuação, caracteres especiais, espaços ou similares
para nomes de classes, atributos, métodos, arquivos, diretorios e etc..

OBS: Quando estamos planejando software e definimos quais Classes teremos que ter no sistema,
chamamos esses objetos que serão mapeador para classes de entidades
"""


class Lampada:
    pass  # passe, nao execute nada mas mantenha o bloco


class ContaCorrente:
    pass


class Produto:
    pass


class Usuario:
    pass


lamp = Lampada()

print(type(lamp))


# exemplo de utilizações de classes que ja fazemos e não percebemos
valor = int('42')  # Cast
# O INT É UMA CLASSE PYTHON
print(type(valor))

# Apenas nossas classes são feitas com as iniciais maisculas
# As classes do python são feitas minusculas
# Justamente pra diferenciar uma classe interna do Python de uma criada por nos
