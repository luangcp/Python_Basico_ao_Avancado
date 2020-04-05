"""
POO - Polimorfismo

Poli -> Muitas
Morfis -> Formas

Objetos que podem ter muitas formas / se comportar de formas diferentes

Quando a gente reimplementa um método presente na classe pai em classes filhas
estamos realizando uma sobrescrita de método (Overriding)

O overriding é a melhor representação do polimorfismo

"""


class Animal(object):  # LEMBRANDO QUE POR PADRAO TODA CLASSE EM PYTHON HERDA OBJECT,

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        # raise é uma exceção
        raise NotImplementedError('A classe filha precisa implementar este metodo')

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala auau')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala mial')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala atiititti')


# TESTES

felix = Gato('Felix')
felix.comer()
felix.falar()


hulk = Cachorro('Hulk')
hulk.comer()
hulk.falar()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()