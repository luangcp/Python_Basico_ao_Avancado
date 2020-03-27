"""
Debugando codigo com PDB

PDB -> Python Debuguer

Bug -> Inseto 'Historia da computação kkkkk'


"""
# A utilização do print para debugar codigo é uma pratica ruim


def dividir(a, b):
    print(f'A={a} e B= {b}')
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor Incorreto'
    except ZeroDivisionError:
        return 'Não é possivel realizar uma divisão por 0'


print(dividir(4, 7))

print('\n')

"""
Existem formas mais profissionais de se fazer esse 'debug', utilizando o
debugger. Em python, podemos fazer isso em diferentes IDEs, com o Pycharm 
ou utilizando o PDB - Python Debugger
"""
# Repare que clicando na linha ele seleciona, dps é so fazer o debug
# Exemplo com o Pycharm


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor Incorreto'
    except ZeroDivisionError:
        return 'Não é possivel realizar uma divisão por 0'


# Exemplo com PDB
"""
Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb
e então utilizar a função set_trace()

* A partir do python 3.7 não é mais necessario importar a biblioteca pdb
pois o comando foi incorporado como função built-in (integrada) 
chamada de breakpoint()


COMANDOS BASICOS PDB:
 l - (listar onde estamos no codigo)
 n - (proxima linha)
 p - (imprime variavel) 
 c - (continua a execução - Finaliza o debugging)
"""
# Exemplo 1 PDB

# import pdb

nome = 'Luan'
sobrenome = 'Pinheiro'
# pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Engenharia de Controle e Automação'
final = nome_completo + ' ' + 'Faz o curso' + curso
print(final)

# Exemplo 2 PDB:

nome = 'Luan'
sobrenome = 'Pinheiro'
# import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Engenharia de Controle e Automação'
final = nome_completo + ' ' + 'Faz o curso' + curso
print(final)


# Porque utilizar esse formato?
"""
O debug é utilizado durante o desenvolvimento.
Costumamos realizar todos os imports de bibliotecas no inicio do arquivo
então é melhor colocar o import e o set_trace() somente no lugar que vai utilizar
pq dps vai tirar 
Colocamos onde vamos debbugar

Após finalizar apaga a linha e ta pronto o codigo
"""

# Exemplo 3 Utilizando breakpoint():
nome = 'Luan'
sobrenome = 'Pinheiro'
breakpoint()  # Utilizando o braakponit (com ele nao precisa importar nada)
nome_completo = nome + ' ' + sobrenome
curso = 'Engenharia de Controle e Automação'
final = nome_completo + ' ' + 'Faz o curso' + curso
print(final)

# OBS: cuidados com os conflitos entre os nomes de variaveis e os comandos do pdb

# Exemplo solucionando possivel problema de conflito de variaveis:


def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

# No exemplo acima vai dar conflito
# Os nomes das variaveis sao os mesmos dos comandos
# Para resolver o problema é so utilizar o comando 'p'
# o comando 'p' imprime as variaveis, só fazer p + nome da variavel

# Nada de colocar nomes não representativos nas variaveis
# Sempre optar por nomes significativos como num1, num2, num3
