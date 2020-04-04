"""
Trabalhando com deltas de Data e Hora

delta = diferença entre uma data e outra
diferença entre data final e data inicial

"""
import datetime

# data de hoje
data_hoje = datetime.datetime.now()

# data para ocorrer um determinado evento no futuro
aniversario = datetime.datetime(2021, 3, 3, 0)

# calculando o delta
tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))
print(repr(tempo_para_evento))
print(f'O tempo até o evento é de: {tempo_para_evento}')

print(f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds //60 //60} horas')

# ------------------------------------------------------------------------------------
print('\n')

data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=15)  # O boleto vence daqui 15 dias

print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto

print(f' A data de vencimento do boleto é {vencimento_boleto}')  # a data de vencimento
