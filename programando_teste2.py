"""
Fazer um programa de cadastro de rede social
"""
print('-------Bem-Vindo a nova Rede Social Do GALO GalON-------')
print('ESCOLHA O QUE DESEJA FAZER: \n')
print('1 - Para entrar na sua conta digite ')
print('2 - Para criar uma nova conta digite ')
print('3 - Para saber mais digite ')
escolha = ''
if escolha == 1:
    print('Digite seu nome de usuario')
    usuario = input('')
    print('Digite sua senha')
    senha = input('')
    print('ESCOLHA O QUE DESEJA FAZER: \n')
    print('1 - Comprar ingressos ')
    print('2 - Bate papo ')
    print('3 - noticias ')
    print('Entrar em contato')
    while escolha != 'sair' or 'Sair':
        if escolha == '1':
            print('Não há ingressos de jogos disponiveis no momento, acompanhe as novidades por email')
        elif escolha == '2':
            print('Bem-vindo ao bate papo')
        elif escolha == '3':
            print('Noticias sobre o GALÃO DA MASSA:')
        else:
            print('ERRO')
            break
print('Volte sempre')

if escolha == '2':
    nome = input('Escreva seu nome completo \n')
    nome_usuario = input('Escreva o nome de usuario desejado')
    senha_escolhida = input('Escolha sua senha')
    senha2 = input('Confirme a senha escolhida:')
    if senha2 != senha_escolhida:
        print('As senhas não são iguais, por favor tente novamente')
    if senha2 == senha_escolhida:
        print(f'Seu cadastro está feito! Seja bem vindo {nome_usuario}')


if escolha == '3':
    print(' O GalON foi desenvolvido em março de 2020 por Luan Pinheiro, com intuito de conectar, e possibilitar o '
          'compartilhamento de dados entre atleticanos, além de venda de camisas, ingressos e acompanhamento de todas'
          'as noticias sobre o nosso GALÃO DA MASSA')


