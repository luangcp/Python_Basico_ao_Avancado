"""
Try / Except / Else / Finally

Dica de quando e onde tratar codigo:

- TODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuario é DESTRUIR seu sistema

* A utilização de else e finally não é tão comum

Else -> é executado somente se não ocorrer o erro

Finally -> o bloco finally é sempre executado, Independente se houve exceção ou não
O finally geralmente é utilizando, para fechar ou desalocar recursos.

"""
# -*- coding: UTF-8 -*-
# Exemplo de utilidade try e except
try:
    num = int(input('Informe um número: '))
    print(f'Você digitou {num}')
except ValueError:
    print('Era esperado que você digitasse um numero')

# Utilizando com else

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Era esperado que você digitasse um numero')
else:  # é executado se nao ocorrer o erro
    print(f'Você digitou {num}')

# Utilizando o Finally

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Era esperado que você digitasse um numero')
else:  # é executado se nao ocorrer o erro
    print(f'Você digitou {num}')
finally:  # é executado o finally
    print("Executando o finally")

# Exemplos mais complexos MAL FEITO


def dividir(a, b):
    return a/b


try:
    num1 = int(input('Entre com o valor do numero 1'))
    num2 = int(input('Entre com o valor do numero 2'))
    print(dividir(num1, num2))
except ValueError:
    print('O valor precisa ser numerico')

# Exemplo complexo BEM FEITO:
# O tratamento é feito na função!


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor Incorreto'
    except ZeroDivisionError:
        return 'Não é possivel realizar uma divisão por 0'


num1 = int(input('Entre com o valor do numero 1'))
num2 = int(input('Entre com o valor do numero 2'))
print(dividir(num1, num2))
