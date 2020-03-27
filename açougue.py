"""
Autor: Luan Pinheiro
Data: 21/01/2020
Programa referente a brincadeira feita no grupo sobre criar um açougue online

"""
produto = ''
compras = []
picanha = 30
alcatra = 25
frango = 20
total = 0
while produto != 'sair':
    print('-----------Bem-vindo ao açougue corote, a seguir estão os produtos disponiveis----------- \n')
    print('Carne de picanha = R$ 30,00 ')
    print('Carne de alcatra = R$ 25,00 o Kg ')
    print('Frango Assado = R$ 20,00 a unidade ')
    # print(' ')  # Para adicionar outros produtos remova o comentario antes de print
    print('Adicione os produtos no carrinho e para encerrar escreva "sair" ')
    produto = input()
    if produto != 'sair':
        compras.append(produto)
        if produto == 'picanha' or 'carne de picanha' or 'Carne de picanha' or 'Picanha':
            total = total+30
        elif produto == 'alcatra' or 'carne de alcatra' or 'Carne de alcatra' or 'Alcatra':
            total = total + 25
        elif produto == 'frango' or 'frango assado' or 'Frango assado' or 'Frango':
            total = total + 20
        else:
            print('Não possuimos esse produto')
for produto in compras:
    print(f'As suas compras são: {produto}')
    print(f'O total a pagar é: {total}')
    pagamento = input('Qual a forma de pagamento? \n 1- Dinheiro \n 2- Cartão \n')
    if pagamento == '1' or 'dinheiro' or 'Dinheiro':
        print("Pagamento em dinheiro \n ")
        endereco = input('Digite seu endereço: \n')
        print(f'Certo, a seu pedido foi confirmado e será entregue em {endereco} o entregador receberá o dinheiro\n')
        break
    if pagamento == '2' or 'Cartao' or 'cartao':
        print("Pagamento em cartão \n ")
        endereco = input('Digite seu endereço: \n')
        print(f'Certo, a seu pedido foi confirmado e será entregue em {endereco} o entregador levará a maquininha\n')
        break
    else:
        print('Invalido')
print('Fim')
