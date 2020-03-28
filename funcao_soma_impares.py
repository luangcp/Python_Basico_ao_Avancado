"""
Função soma impares utilizada para ser importada em Dunder Main e Dunder name


"""


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num  # Total = numero de numeros na lista + numeros de numeros impares na lista
    return total  # O return deve estar exatamente onde o for finaliza, para que funcione corretamente


if __name__== '__main__':
    lista = [1, 2, 3, 4, 5, 6]
    print(soma_impares(lista))
else:
    print('COMO FOI FEITO:'
          'LEMBRE-SE QUE FOI FEITO UTILIZANDO O __name__')