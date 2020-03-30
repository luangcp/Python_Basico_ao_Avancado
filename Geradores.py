"""
Geradores

- Geradores (Generators) são iterators (iteradores)

OBS: O contrario não é verdadeiro, ou seja, nem todo iterator é um generator

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com expressões geradoras

Diferenças entre Funções e Generator Functions (funções geradoras)

-----------------------------------------------------------------------------------------
| Funções                                   | Generator Functions  |
----------------------------------------------------------------------------------------
 Utilizam Return                     I                 Utilizam yield
                                     I
 Retorna uma vez                     I              Podem utilizar yield multiplas vezes
                                     I
 Quando executada, retorna um valor  I           Quando execurata, retorna um generator
 ---------------------------------------------------------------------------------------


"""

# Exemplo de Generator Function:


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador  # Retorna o valor e aguarda ate uma função next ser chamada novamente
        contador = contador + 1

# OBS: Uma Generator Function não é um Generator. Ela gera um generator.


gen = conta_ate(5)

print(type(gen))

# Aplicando a função next

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# o yield não sai da função enquanto nãoo for finalizado
print('\n')

gen = conta_ate(10)

for num in gen:
    print(num)

# o yield faz a contagem de um em um ate finalizar, até passar o next em todas
# No caso do for ele passa o next em tds por baixo dos panos