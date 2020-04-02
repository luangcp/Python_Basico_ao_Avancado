"""
POO - Propriedades - Properties

Em linguagens de programação como o JAVA ao declararmos atributos privados nas classses
costumamos a criar metodos publicos para manipulação desses atributos. Esses metodos
são conhecidos por getters e setters , onde os getters retornam o valor do atributo
e os setters alteram o valor do mesmo
"""

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular} '

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        return self.__titular == titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        return self.__limite == limite


conta1 = Conta('Luan', 3000, 5005)
conta2 = Conta('Viviane', 1500, 6000)

print(conta2.extrato())
print(conta1.extrato())

# pra somar o saldo de todas as contas

# OBS: Isso nunca deve ser feito, mas é possivel:
# Se ele é privado o acesso tem que ser só la dentro
soma = conta1._Conta__saldo + conta2._Conta__saldo
print(f'A soma do saldo das contas é {soma}')


"""
A MELHOR FORMA DA GENTE TER ACESSO A VALORES DE ATRIBUTOS É CRIANDO METODOS PARA MANIPULALOS
CHAMADOS GETTERS E SETTERS

get significa pegar
set 
"""
# Então fica

soma1 = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma das duas contas é {soma1}')

print(conta1.__dict__)
conta1.set_limite(9999999)
print(conta1.__dict__)

print('\n\n')

print('UTILIZANDO PROPRIEDADES')
# ---------------------------------------------------------------------------
# pra criar propriedades utilizamos um decorator @property


class Conta1:  # 1° declara a classe

    contador = 0  # 2° atributos de classe

    def __init__(self, titular, saldo, limite):  # 3° construtores e seus atributos
        self.__numero = Conta1.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta1.contador += 1

    @property  # property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    # Criando um set pro limite
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):  # metodos de instancia
        return f'Saldo de {self.__saldo} do cliente {self.__titular} '

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite


conta3 = Conta1('Hulk', 4000, 6400)
conta4 = Conta1('Francisco', 3333, 5595)

print(conta3.extrato())
print(conta4.extrato())

soma2 = conta3.saldo + conta4.saldo
print(f'A soma do saldo das contas é {soma2}')

# por padrão uma propriedade é um getter

print(conta3.__dict__)
conta3.limite = 76543
print(conta3.__dict__)
print(conta3.limite)

print(conta3.valor_total)
print(conta4.valor_total)