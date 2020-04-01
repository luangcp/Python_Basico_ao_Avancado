"""
Criando um gerenciamento de banco utilizando classes
"""
from random import randint
from passlib.hash import pbkdf2_sha256 as cryp  # Biblioteca de encriptografar

class Conta:

    contador = randint(400, 999)
    saldo = 0
    limite = 500

    def __init__(self, titular, cpf, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.cpf = cpf
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'             Olá {self.titular} seu saldo é de {self.saldo} reais, com limite de {self.limite} reais\n')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


print('Bem Vindo! Estamos prontos para criar a sua conta!!\n')
print('-------------------------------------------------------------')
titular1 = str(input('Escreva seu nome e sobrenome: '))
cpf1 = str(input('Informe seu cpf somente numeros : '))
senha1 = str(input('Escolha sua senha: '))
confirma_senha = str(input('Confirme a senha: '))

if senha1 == confirma_senha:
    print('Senha confirmada \n')
else:
    print('Senha não confere..')
    exit(42)
print('---------------------------------------------ATENÇÃO----------------------------------------------------------')
print('                          O banco informa que sua conta começa sem saldo e com limite de 500 reais           \n')

conta1 = Conta(titular1, cpf1, saldo=0, limite=500)
conta1.extrato()

print('Para depositar algum valor digite 1')
print('Para sacar algum valor digite 2')
print('Para outras opções digite 3')
escolha = int(input())


if escolha == 1:
    deposito = int(input('Escreva o valor do deposito'))
    conta1.depositar(deposito)
    print(f'Certo agora seu saldo é de {conta1.saldo} ')
    print('Deseja sacar algum valor? Se sim digite 1, se não digite 2')
    escolha3 = int(input())
    if escolha3 == 1:
        saque = int(input('Escreva o valor do saque desejado'))
        if saque > conta1.saldo:
            print('Saque não permitido, você não tem esse valor em conta')

        else:
            conta1.sacar(saque)
            print(f'Seu novo saldo é de {conta1.saldo}')
    elif escolha3 == 2:
        pass

elif escolha == 2:
    saque = int(input('Escreva o valor do saque desejado'))
    if saque > conta1.saldo:
        print('Saque não permitido, você não tem esse valor em conta')

    else:
        conta1.sacar(saque)
        print(f'Seu novo saldo é de {conta1.saldo}')

elif escolha == 3:
    pass

else:
    print('Escolha invalida')


print('Para saber os detalhes da sua conta digite 4')
print('Para encerrar a operação digite 5')
escolha2 = int(input())


if escolha2 == 4:
    conta1.extrato()

elif escolha2 == 5:
    pass

else:
    print('Escolha invalida')