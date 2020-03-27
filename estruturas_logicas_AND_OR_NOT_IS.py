"""
Estruturas lógicas: and (e), or (ou), not (não), is(é)

Operadores unários:
    - not
Operadores binarios:
    - and, or, is

Regras de utilização:
Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True vira False, se for False vira True
Para o 'is', o valor é comparado com um segundo.
"""

ativo = True
logado = True

print("Tentando a estrutura and: \n")
# Para and
if ativo and logado:
    print('Bem vindo usuario!!\n\n')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu email \n\n')

# -----------------------------------------------------------------------

print("Tentando a estrutura or: \n")
# Para or
if ativo or logado:
    print('Bem vindo usuario!! \n\n')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu email \n\n')

# ----------------------------------------------------------------------

print("Tentando a estrutura not: \n")
# Para not, precisa apenas de um valor
if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu email\n\n')
else:
    print('Bem-vindo usuário!! \n\n')

# Relembrando
print(not False)
print(not True, '\n')

# ----------------------------------------------------------------------

print("Tentando a estrutura is: \n")
# Para is
if ativo is False:
    print('Bem-vindo usuário!! \n\n')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu email \n\n')

# Ativo é falso?
print(ativo is False)

# Ativo é Verdadeiro?
print(ativo is True)