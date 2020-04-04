"""
Manipulando Data e Hota

Python tem um modulo built-in (integrado) para se trabalhar com dara e hora
chamado datetime

"""
import datetime

print(dir(datetime))  # coisa que datatime pode fazer

print(f'O ano maximo que o datetime pode funcionar é {datetime.MAXYEAR}')
print(f'O ano minimo que o datetime pode funcionar é {datetime.MINYEAR}')

# Retorna a data e hora corrente
print(datetime.datetime.now())  # -> 2020-04-03 19:42:25.646082

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))  # -> datetime.datetime(2020, 4, 3, 19, 43, 39, 540816)

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)

# Alterar o horario para 16 horas
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)
# podemos mudar qualquer parametro, data, hora, ano

# Criando uma data/hora

evento = datetime.datetime(2019, 1, 1, 0)
print(type(evento))  # DATATIME
print(type('31/12/2019'))  # STRING
print(evento)
print('\n')

# COMO ENTÃO RECEBER DADOS DE UM USUARIOS E TRANSFORMAR PRA HORA

aniversario = input('Informe sua data de nascimento (dd/mm/yyy): ')

print(aniversario)
print(type(aniversario))

# vamos converter

aniversario = aniversario.split('/')  # cria um array separando cada elemento pela barra

print(aniversario)  # virou uma lista de string
print('\n')


aniversario = datetime.datetime(int(aniversario[2]), int(aniversario[1]), int(aniversario[0]))
print(aniversario)
print(type(aniversario))

# Acesso individual dos elementos de data e hora

print(evento.year)  # ano
print(evento.month)  # mes
print(evento.day)  # dia
print(evento.hour)  # hora
print(evento.minute)  # minuto
print(evento.second)  # segundo
print(evento.microsecond)  # microsegundo