"""
Criando a propria versão de loop

o python tem os loops for, while
mas pode criar a propria versão
"""

for num in [1, 2, 3, 4, 5]:  # POR BAIXO DOS PANOS iter([1, 2, 3, 4, 5, 6])
    print(num)

print('\n')

for letra in 'Luan Pinheiro':
    print(letra)


# Criando uma versão propria do loop

def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Hulk')

numeros = 1, 2, 3, 4, 5

meu_for(numeros)

