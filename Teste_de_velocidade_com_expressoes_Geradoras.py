"""
Teste de velocidade com expressões geradoras


"""

# Generators (geradores)


def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()

print(ge1)

print(next(ge1))
print(next(ge1))

# Generators expression

ge2 = (num for num in range(1, 10))

print(ge2)

print(next(ge2))
print(next(ge2))


# outras coisas
# Imprime pra mim a soma dos numeros de 1 a 10
print(sum(num for num in range(1, 10)))

# Usando teste de velocidade
import time

# Generator expression  -> 1.0178849697113037

gen_inicio = time.time()
print(sum(num for num in range(10000000)))
gen_tempo = time.time() - gen_inicio


# List Comprehension  -> 1.0354647636413574

list_inicio = time.time()
print(sum([num for num in range(10000000)]))
list_tempo = time.time() - list_inicio

print(f'Generator expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')


# Generation é mais rapido

# Conclusão: Generation é mais rapido e ocupa menos memoria

