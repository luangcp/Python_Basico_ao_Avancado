"""
**kwargs

Poderiamos chamar esse parametro de **x mas por convenção chamamos de **kwargs

Este é so mais um parametro, mas diferente do *args que coloca os valores extras
em uma tupla, o **kwargs exige que utilizemos parametros nomeados, e transforma esses
parametros extras em um dicionario

"""


def cores_favoritas(**kwargs):
    print(kwargs)


print(cores_favoritas(marcos='verde', julia='azul', luan='verde',
                      viviane='branco'))

print('\n')

# Outro exemplo:


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


print(cores_favoritas(marcos='verde', julia='azul',
                      luan='verde', viviane='branco'))

"""
OBS: Os parametros *args e **kwargs não são obrigatorios

tantos faz eu fazer isso:
cores_favoritas()
ou:
cores_favoritas(luan='verde)
"""
print('\n')

# Outro exemplo:


def cumprimento_especial(**kwargs):
    if 'luan' in kwargs and kwargs['luan'] == 'Python':
        return 'Voce recebeu um cumprimento pythonico Luan'
    elif 'luan' in kwargs:
        return f"{kwargs} ['luan']"
    return 'Não tenho certeza de quem você é'


print(cumprimento_especial())
print(cumprimento_especial(luan='Python'))
print(cumprimento_especial(luan='Oi'))
print(cumprimento_especial(luan='Orangotango'))

"""
Nas nossas funções podemos ter (NESTA ORDEM):
- Parametros obrigatorios;
- *args
- Parâmetros default (não obrigatorios);
- **kwargs
"""
print('\n')


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(20, 'Luan', 'é atleticano', 1, 3, 4, solteiro=False)
minha_funcao(18, 'Luan', eu='Não', voce='Vai')
minha_funcao(19, 'Viviane', 9, 4, 3, java=False, python=True)

print('\n')


"""
Entenda pq é importante manter a ordem dos parametros na declaração

def mostra_info(a, b, *args, instrutor='Luan', **kwargs:
    return [a, b, args, instutor, kwargs]
    
    
 # a = 1
 # b = 2
 args = (4,)
 instrutor = 'Luan'
 kwargs = {'sobrenome': 'Luan', 'cargo': 'Instrutot')
 
 
print(mostra_info(1, 2, 4, sobrenome='Pinheiro', cargo='Instrutor'))

"""


def mostra_info(a, b, *args, instrutor='Luan', **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 4, sobrenome='Pinheiro', cargo='Instrutor'))


# Se fazer a declaração errada as informações vão ficar todas bagunçadas
# Mimimi aula chata essa

print('\n')

# Desempacotar co kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs}['nome'] {kwargs}['Sobrenome']"


nomes = {'nome': 'Luan', 'sobrenome': 'pinheiro'}
print(mostra_nomes(**nomes))  # Com o duplo asteristico desempacota

print('\n')

# Outro exemplo:


def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = 1, 2, 3
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)  # Dicionario é com dois asteristicos

# Por ultimo

soma_multiplos_numeros(**dicionario)
