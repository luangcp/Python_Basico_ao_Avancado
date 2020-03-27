"""
Testando o uso de função

Montando uma calculadora com funções
"""
# Funções:


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor Incorreto'
    except ZeroDivisionError:
        return 'Não é possivel realizar uma divisão por 0'


def multiplicar(a, b):
    try:
        return int(a) * int(b)
    except ValueError:
        return 'Valor incorreto'


def soma(a, b):
    try:
        return int(a) + int(b)
    except ValueError:
        return 'Valor incorreto'


def subtracao(a, b):
    try:
        return int(a) - int(b)
    except ValueError:
        return 'Valor incorreto'


# Execução da calculadora
print('Bem vindo a calculadora:')
num1 = int(input('Entre com o valor do numero 1'))
num2 = int(input('Entre com o valor do numero 2'))

print('ESCOLHA: \n Para divisão digite: 1 \n'
      'Para multiplicação digite: 2 \n'
      'Para soma digite: 3 \n'
      'Para subtração digite: 4')

escolha = int(input())
if escolha == 1:
    print(f'Você escolheu divisão \n')
    print(f'O resultado é {dividir(num1, num2)}')
elif escolha == 2:
    print(f'Você escolheu multiplicação \n')
    print(f'O resultado é {multiplicar(num1, num2)}')
elif escolha == 3:
    print(f'Você escolheu soma \n')
    print(f'O resultado é {soma(num1, num2)}')
elif escolha == 4:
    print(f'Você escolheu subtração \n')
    print(f'O resultado é {subtracao(num1, num2)}')
else:
    print('Por favor escolha um valor valido')