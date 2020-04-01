"""
POO - Objetos

Objetos -> São instancias da classe. Ou seja, apos o mapeamento do objeto do mundo
real para sua representação computacional, devemos poder criar quantos objetos forem
necessarios. Podemos pensar nos objetos/instancias de uma classe como variaveis de tipo
definido na classe.
"""


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):  # metodo para checar se a lampada ta ligada
        return self.__ligada

    def ligar_desligar(self):  # metodo para ligar e desligar a lampada
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz oi')


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo,cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha




# Instancias/Objetos
lamp1 = Lampada('branca', 110, 60)
print(f'A lampada está ligada? {lamp1.checa_lampada()}')  # chegando se a lampada ta ligada
lamp1.ligar_desligar()   # Ligando ou desligando
print(f'A lampada está ligada? {lamp1.checa_lampada()}')  # chegando se a lampada ta ligada

cliente1 = Cliente('Luan Pinheiro', '136.286.176-69')
conta1 = ContaCorrente(5000, 30000, cliente1)

print(conta1.mostra_cliente())

conta1._ContaCorrente__cliente.diz()

# A instancia da classe nada mais é do que um objeto do tipo da clase