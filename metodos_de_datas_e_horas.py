"""
Metodos de Data e Hora

now -> trás a hora e data de agora, com beneficio de poder escolher o fusuhorario (timezone)
today -> trás a hora e data de agora.
combine() -> da pra fazer uma manutenção programada, combinar horarios etc..
weekday() -> encontrar o dia da semana
strftime() -> Formatar o formato de data dd/mm/yyy ou yyy/mm/dd
strptime() -> Transformando uma string num objeto do tipo datetime
datetime.time -> somente a hora
"""
import datetime

# Com now podemos especificar um timezona (fusohorario)
agora = datetime.datetime.now()  # now == agora
print(agora)
print(type(agora))
print(repr(agora))

print('\n')

hoje = datetime.datetime.today()  # today == hoje
print(hoje)
print(type(hoje))
print(repr(hoje))
print('\n')
# A DIFERENÇA ENTRE NOW E TODAY É QUE NO NOW PODEMOS ESCOLHER A TIMEZONE Ex: Brasil, Eua etc..


# Mudança ocorrendo à meia noite combine()

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=10)), datetime.time())
print(manutencao)
print(type(manutencao))
print(repr(manutencao))
print('\n')

# Encontrar o dia da semana, weekday()

# Os dias da semana do metodo weekday começam em 0, sendo esta a segunda feita

"""
0- Segunda feita (Monday)
1 - Terça feira (Tuerday)
2 - Quarta Feira (Wednesday)
3 - Quinta Feira (Thuresday)
4 - Sexta (friday)
5 - Sabado (saturdey)
6 - domingo (sunday)
"""
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=9)), datetime.time())
print(manutencao.weekday())
if manutencao.weekday() == 0:
    print('Segunda')
elif manutencao.weekday() == 1:
    print('Terça')
elif manutencao.weekday() == 2:
    print('Quarta')
elif manutencao.weekday() == 3:
    print('Quinta')
elif manutencao.weekday() == 4:
    print('Sexta')
elif manutencao.weekday() == 5:
    print('Sabado')
elif manutencao.weekday() == 6:
    print('Domingo')
else:
    print('ERRO')

# ---------------------------------------------------------------

aniversario = input('Qual sua data de aniversario dd/mm/aa ?: ')

aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Você nasceu na Segunda')
elif aniversario.weekday() == 1:
    print('Você nasceu na Terça')
elif aniversario.weekday() == 2:
    print('Você nasceu na Quarta')
elif aniversario.weekday() == 3:
    print('Você nasceu na Quinta')
elif aniversario.weekday() == 4:
    print('Você nasceu na Sexta')
elif aniversario.weekday() == 5:
    print('Você nasceu no Sabado')
elif aniversario.weekday() == 6:
    print('Você nasceu no Domingo')
else:
    print('ERRO')

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------


def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'
    else:
        print('erro')

# Formatando datas/horas com strftime() (String Format Time)
# dd/mm/yyy


hoje = datetime.datetime.today()
print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%Y')
hoje_formatado2 = hoje.strftime('%d de %B de %Y')

print(hoje_formatado)
print(hoje_formatado2)
print('\n')


# utilizando a função
print(formata_data(hoje))
print('\n')


# FAZENDO COM pip install textblob
from textblob import TextBlob

# OBS: PRECISA DE INTERNET PARA FUNCIONAR


def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"


hoje = datetime.datetime.today()
print(formata_data(hoje))

# Transformando uma string num objeto do tipo datetime

# nascimento = datetime.datetime.strptime('19/04/2020', '%d/%m/%Y')

nascimento1 = input('Qual sua data de nascimento? dd/mm/aaa: ')

nascimento = datetime.datetime.strptime(nascimento1, '%d/%m/%Y')
print(nascimento)

# ---------------------------------------------------------------------------------------------

print('\n')

# somente a hora:

almoco = datetime.time(12, 30, 0)
print(almoco)
print('\n')

# Marcando tempo de execução do programa
import timeit

# calcule o tempo disso

# loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=1000)
print(f'O tempo gasto no loop foi: {tempo}')

# List Comphension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=1000)
print(f'O tempo gasto no list comphension foi: {tempo}')

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=1000)
print(f'O tempo gasto com map foi: {tempo}')

import functools


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


print(timeit.timeit(functools.partial(teste, 2), number=10000))

