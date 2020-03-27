"""
O bloco Trt/Except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso codigo
previnindo assim que o programa pare de funcionar e o usuario receba mensagens
de erro inesperadas

try:
    //execução problematica
except:
    //o que deve ser feito em caso de problema

OBS: Tratar erro de forma generica não é a melhor forma de tratamento de erros.
O ideal é SEMPRE tratar de forma especifica
"""

# Exemplo 1 - Tratando um erro generico

try:
    luan()
except:
    print('Deu algum erro')

# Tente executar a função luan e caso vc encontre erros, imprima a mensagem

# Exemplo 2 - Tratando um erro generico

try:
    len(5)
except:
    print('Deu algum problema')

print('\n')

# Exemplo 3 - Tratando um erro especifico

try:
    pudim()
except NameError:
    print('Voce esta utilizando uma função inexistante')

# Exemplo 4 - Tratando um erro especifico
# try:
#    len(5)  # Não é name error
# except NameError:
#    print('Voce esta utilizando uma função inexistante')

# Exemplo 5: Dando um nome pro erro (err)

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro {err}')

# Exemplo 6 - Podemos efetuar diversos tratamentos de erros de uma vez.

print('\n \n')
try:
    print('luan'[9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:  # EXTENÇÃO MT AMPLA PEP 8
    print('Deu um erro diferente')
print('\n')
# Exemplo 7 - Utilizando tratamento de erro na função


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None


dic = {"nome": "Luan"}

print(pega_valor(dic, "game"))


