from random import random  # Importando do pacote random a função random


def pedra_papel_tesoura():
    # Gera um numero pseudo-randomico entre 0 e 1 (pseudo- randomica pode ter repetição)
    valor = random()  # Numeros randomicos trazem a ideia de aletoriedade
    if valor > 0.3:
        return 'Pedra'
    if valor < 0.3:
        return 'Tesoura'
    if valor > 0.4:
        return 'Papel'
    return 'outro'


print(pedra_papel_tesoura())