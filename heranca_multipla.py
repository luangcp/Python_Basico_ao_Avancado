"""
POO - Herança multipla

# No java podemos herdar apenas uma classe, uma classe herddndo de outra
# No python podemos herdar multiplas classes

Herança multipla nada mais é do que a possibilidade de uma classe herdar de multiplas classes
fazendo que a classe filha herde todos os atributos e metodos de todas as clases herdadas

OBS: A herança multiplia pode ser feita de duas maneiras:
    - Por multiderivação direta;
    - Por multiderivação indireta;

OBS: Não importa se a derivação é direta ou indireta, A classe que realizar
a herança herdará todos os atributos e métodos das super classes.
"""

# Exemplo 1 - Multiderivação Direta


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class Multiderivada(Base1, Base2, Base3):
    pass


# EXEMPLO 2 - Multiderivação indireta

class Base4:
    pass


class Base5(Base4):
    pass


class Base6(Base4):
    pass


class Multiderivada2(Base6):
    pass


"""
OBS: Não importa se a derivação é direta ou indireta, A classe que realizar
a herança herdará todos os atributos e métodos das super classes.
"""

# EXEMPLO REAL


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self,nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} esta nadando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra'


class Pinguim(Terrestre, Aquatico):  # ordem de herança

    def __init__(self, nome):
        super().__init__(nome)


# Testando
baleia = Aquatico('Shand')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Rodrigo')
print(tatu.andar())
print(tatu.cumprimentar())

pinguim = Pinguim('Alessandra')
print(pinguim.andar())
print(pinguim.nadar())
print(pinguim.cumprimentar())  # Method Resolution Order - MRO

# Descobrir se o objeto é uma instancia de outro objeto

print(f' pinguim é instancia de Pinguim? {isinstance(pinguim, Pinguim)}')  # True
print(f' pinguim é instancia de Aquatico? {isinstance(pinguim, Aquatico)}')  # True
print(f' pinguim é instancia de Terrestre? {isinstance(pinguim, Terrestre)}')  # True
print(f' pinguim é instancia de Animal? {isinstance(pinguim, Animal)}')  # True
print(f' pinguim é instancia de object? {isinstance(pinguim, object)}')  # True


