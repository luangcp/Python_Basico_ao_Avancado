"""
POO - Abstração e Encapsulamento

O grande objetivo da Programação orientada a objeto, é encapsular nosso codigo
dentro de um grupo lógico e hierárquico utilizando classes

Encapsular -> capsula

                classe
----------------------------------------
|                                       |
|      atributos e metodos              |
|                                       |
_________________________________________

# Relembrando Atributos/Metodos Privados em Python

Imagine que temos uma classe chamada Pessoa, contendo
um atributo privado chamado __nome e um metodo privado
chamado __falar().

Esses elementos privados só devem/deveriam ser acessados
dentro da classe. Mas python não bloqueia este acesso
fora da classe. Com python acontece um fenomeno chamado
Name Mangling. Que faz uma alteração na forma de se acessar
os elementos privados, conforme:

_Classe__elemento

exemplo - Acessando elementos privados fora da Classe:

instancia._Pessoa__nome
instancia._Pessoa__falar()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe,
escondendo atributos e metodos privados de usuarios

"""

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


# Testando

conta1 = Conta('Luan', 150.00, 1500)

# o acesso está publico
print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)

# com o acesso a conta publico, é possivel fazer alterações na conta alem de acessalas com facilidade
# isso é inseguro e não recomendado


conta1.extrato()

# E SE FOSSE COM OS ATRIBUTOS PRIVADOS??

class Conta2:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor deve ser positivo')

    def transferir(self, valor, conta_destino):
        # 1- Remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10  # Taxa de transferencia paga por quem fez a transferencia

        # 2- Adicionar o valor na conta de destino
        conta_destino.__saldo += valor


# Para acessar os dados daria somente com o Name Mangling

conta2 = Conta2('Luan', 200, 2000)
print(conta2.__dict__)
conta2.extrato()

print(conta2._Conta2__titular)  # Name Mangling

conta2._Conta2__titular = 'Viviane'  # mudando o nome de um atributo privado com magling
print(conta2.__dict__)

# lembrando que esse acesso é errado, mas o python permite, está nas maos do desenvolvedor
print('\n')

# outros testes

conta2.depositar(150)  # funciona
print(conta2.__dict__)

conta2.sacar(200)

conta3 = Conta2('Luan', 400, 12000)

conta2.extrato()
conta3.extrato()
print('\n')

# COMO TRANSFERIR
# LEMBRANDO QUE COLOCAMOS UMA TAXA DE 10 REAIS PARA TRANSFERENCIA
conta2.transferir(100, conta3)
conta2.extrato()
conta3.extrato()