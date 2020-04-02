"""
POO - MRO - Method Resolution Order

Method Resoluction Order (Resolução de ordem de metodos) é a ordem de
execução dos métodos (quem será executado primeiro)

Em python podemos conferir a ordem de execução dos metodos de 3 formas:
    - Via propriedade da classe __mro__
    - Via metodo mro()
    - Via help
"""

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

tux = Pinguim('Tux')
print(tux.cumprimentar())  # Method Resolution Order - MRO


"""
Pinguim(Aquatico, Terrestre)
Eu sou Tux do Mar!

Pinguim(Terrestre, Aquatico)
Eu sou Tux da Terra!

"""

# Method Resolutions Order só acontece com herança multipla
# A ordem causa impacto