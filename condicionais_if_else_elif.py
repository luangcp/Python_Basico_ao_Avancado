"""
Estruturas condicionais
if, else, elif


"""

idade = int(input("Entre com valor da idade: \n"))


if idade < 18:
    print('Menor de idade')  # O comando do if vem 4 espaços identados
    print(idade)
elif idade == 18:
    print('Tem 18 anos')
else:
    print('Maior de idade')
    print(idade)
