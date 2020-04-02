"""
POO - Herança (inheritence)

A ideia de herança é a de reaproveitar código. Também extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e metodos da classe herdada.

Clienta
    - nome
    - sobrenome
    - cpf
    - renda

Funcionario
    - nome
    - sobrenome
    - cpf
    - matricula

Existe alguma entidade generia o suficiente para encapsular os atributos
e metodos comuns a outras entidades?

OBS: Quando uma classe herda de outra classe, ela herda TODOS os atributos e metodos da classe herdada.

OBS: Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    - Super classe;
    - Classe Mãe;
    - Classe Pai
    - Classe base;
    - Classe generica

Quando uma classe herda de outra classe, ela é chamada:
    [Cliente, Funcionario]
    - Sub classe;
    - Classe filha
    - Classe especifica

# Sobrescrita de Métodos (Overriging)
Ocorre quando reescrevemos um metodo presente na super classe em classe filhas

"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):  # Herança
    """Cliente herda de pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)  # superclasse
        self.__renda = renda


class Funcinario(Pessoa):  # Herança
    """Funcionario herda de pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # superclasse
        self.__matricula = matricula

    def nome_completo(self):
        return f'Funcionario: {self.__matricula} Nome {self._Pessoa__nome}'


cliente1 = Cliente('Luan', 'Pinheiro', '136.276.176.69', 50000)
funcionario1 = Funcinario('Hulk', 'Pinheiro', '136.276.555-88', 235233)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(funcionario1.__dict__)

# ------------------------------------------------------------------------
print('\n')

# Sobrescrita de Métodos (Overriging)

