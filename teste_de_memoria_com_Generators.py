"""
Teste de memoria com generators

A eficiencia de generators é melhor -> Gasta menos memoria
baixo consumo de memoria
lembre-se não é velocidade de processamento

# Sequencia de fibonati
1, 1, 2, 3, 5, 8, 13 ...
"""

# Função usando listas 449 MB


def fibonati_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


# Teste 1 449MB
for n in fibonati_lista(100):
    print(n)

print('\n')
# Função usando geradores


def fibonati_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


# Teste 2 Geradores 2.8MB
for n in fibonati_gen(100):
    print(n)

# Generator ocupa MUITO MENOS MEMORIA
