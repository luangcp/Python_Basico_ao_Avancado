"""
List comprehension - Parte 2

Nós podemos adicionar estruturas condicionais lógicas as nossas list comprehensions

"""
# Exemplo 1

numeros = [1, 2, 3, 4, 5, 6, 7]

pares = [numero for numero in numeros if numero % 2 == 0]

impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorar

# Todo numero par o resto é 0
# Todo numero impar o resto é 1
# O simbolo para saber resto em python é o %

# Qualquer numero par modulo de 2 é 0 e 0 em python é false. not false = true
pares = [numero for numero in numeros if not numero % 2]

# Qualquer numero impar modulo de 2 é 1, e 1 em python é true
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)
print('\n')

# Exemplo 2
# Se for par multiplica por 2 se for impar divide por 2
res = [numero * 2 if numero % 2 ==0 else numero / 2 for numero in numeros]
print(res)