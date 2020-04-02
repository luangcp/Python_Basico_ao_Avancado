"""
POO - O metodo super()

O metodo super() se refere à super classe.


"""


class Animal:  # SUPERCLASSE DA CLASSE CACHORRO
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')


class Cachorro(Animal):  # CLASSE ESPECIFICA/SUBCLASSE

    def __init__(self, nome, especie, raca):
        #  Animal. __init__(self, nome, especie)  # POSSIVEL MAS N RECOMENDADO
        super().__init__(nome, especie)  # RECOMENDADO
        self.__raca = raca


hulk = Cachorro('Hulk', 'Cão', 'Pug')

hulk.faz_som('AUAUAUA O MEU FILHO')