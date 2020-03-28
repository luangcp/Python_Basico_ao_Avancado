# -*- coding: UTF-8 -*-

from random import random  # Importando do pacote random a função random


def joga_moeda():
    # Gera um numero pseudo-randomico entre 0 e 1 (pseudo- randomica pode ter repetição)
    valor = random()  # Numeros randomicos trazem a ideia de aletoriedade
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())
