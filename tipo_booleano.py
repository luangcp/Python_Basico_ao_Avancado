"""
# -*- coding: UTF-8 -*-
Tipo Booleano

Algebra booleana, criada por George Boole

2 constantes, verdadeiro ou falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiuscula


"""
ativo = True

print(ativo)

"""
Operações básicas:
"""

# Negação(not)
"""
Fazendo anegação, se o valor booleano for verdadeiro o resultado sera falso, 
se for falso o resultado será verdadeiro, sempre o contrario.
"""
print(not ativo)

logado = False
# Ou (or)
"""
 É uma operação binaria, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro
 
 True or True -> true
 True or False -> True
 False or True -> True
 False or False -> False
"""
print(ativo or logado)

# E (and)
"""
Também é uma opção binaria, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiro.

True and True -> True
True and False -> False
False and True -> False
False and False -> True

"""

