import datetime

print('Descubra quantos anos você tem: ')

atual = datetime.datetime.now()

aniversario = input('Informe sua data de nascimento (dd/mm/yyy): ')
aniversario = aniversario.split('/')  # cria um array separando cada elemento pela barra
aniversario = datetime.datetime(int(aniversario[2]), int(aniversario[1]), int(aniversario[0]))

idade = (aniversario - atual) * (-1)
print(f'A sua idade em dias é de {idade}')
idade_em_anos = (aniversario.year - atual.year) * (-1)
print(f'A sua idade em anos é de {idade_em_anos}')

if idade_em_anos >= 18:
    print('Você é maior de idade')
elif idade_em_anos < 18:
    print('Você é menor de idade')