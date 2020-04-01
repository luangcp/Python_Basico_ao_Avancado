"""
POO - Atributos

Atributos -> Representam as caracteristicas do objeto, ou seja, pelos atributos
nos conseguimos representar computacionalmente os estados de um objeto.

Em python, dividimos os atributos em 3 grupos:
    - Atributos de instancia;
    -Atributos de Classe;
    -Atributos Dinamicos:

# Atributos de instância: São atributos declarados dentro do metodo construtos
OBS: metodo construtor, é um metodo essencial utilizado para a construção do objeto

# Em java, uma classe Lampada, incluindo seus atributos ficaria mais ou menos:

public class Lampada(){
    private int voltagem;
    provate String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
}

Em python seria:

class Lampada:

    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

Atributos da instancia podem ser publicos ou privados, falamos da visibilidade desses atributos
privados -> so podem ser acessados dentro da propria classe onde foi declarado
publico -> por convenção foi decidido que, todo atributo de uma classe é publico,
ou seja pode ser acessado em, todo o projeto

Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro da propria classe onde esta declarado, utiliza-se
__ duplo underscore no inicio do seu nome
"""

# Classes com atributos de instancia publico:


class Lampada:

    def __init__(self, voltagem, cor):  # metodo init (metodos sao tudo q estão dentro da classe)
        self.voltagem = voltagem  # atributo voltagem
        self.cor = cor  # atributo cor
        self.ligada = False  # atributo ligada

# self = é o objeto que está executando o metodo


class ContaCorrente:
    def __init__(self, numero, limite, saldo):  # metodo init (metodos sao tudo q estão dentro da classe)
        self.numero = numero  # O objeto ContaCorrente no atribyto numero vai receber numero
        self.limite = limite  # O objeto ContaCorrente no atribyto limite vai receber limite
        self.saldo = saldo  # O objeto ContaCorrente no atribyto saldo vai receber saldo

# self = é o objeto que está executando o metodo


class Produto:
    def __init__(self, nome, descricao, valor):  # metodo init (metodos sao tudo q estão dentro da classe)
        self.nome = nome  # O objeto produto no atribyto nome vai receber nome
        self.descricao = descricao  # O objeto produto no atribyto descricao vai receber descricao
        self.valor = valor  # O objeto produto no atribyto valor vai receber valor

# self = é o objeto que está executando o metodo


class Usuario:
    def __init__(self, nome, email, senha):  # metodo init (metodos sao tudo q estão dentro da classe)
        self.nome = nome  # o objeto usuario no atributo nome vai receber nome
        self.email = email  # o objeto usuario no atributo email vai receber email
        self.senha = senha  # o objeto usuario no atributo senha vai receber senha

# self = é o objeto que está executando o metodo
# a palavra self não é obrigada estar ali, é uma convenção utilizada
# usualmente o primeiro nome do parametro é self, podemos colocar outro nome mas n é legal


# Atributos publicos e atributos privados
"""
Atributos da instancia podem ser publicos ou privados, falamos da visibilidade desses atributos
privados -> so podem ser acessados dentro da propria classe onde foi declarado
publico -> por convenção foi decidido que, todo atributo de uma classe é publico,
ou seja pode ser acessado em, todo o projeto

Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro da propria classe onde esta declarado, utiliza-se
__ duplo underscore no inicio do seu nome

também conhecido como Name Mangling
"""
# Atributos publicos e atributos privados


class Acesso:
    def __init__(self, email, senha):
        self.email = email  # se iniciamos o atributo com __ é pq ele é privado
        self.__senha = senha   # se iniciamos o atributo com __ é pq ele é privado

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

"""
OBS: LEMBRE-SE que isso é apenas convenção, ou seja, a linguagem python não
vai impedir que façamos acesso asos atributos sinalizados como privados fora da classe
"""
# Exemplo:

user = Acesso('luan@hotmail.com', '123456')
print(user.email)  # instancia.atributo  SO CONSEGUIMOS O ACESSO AQUI PQ É PUBLICO
try:
    print(user.__senha)  # Atribute error
except AttributeError:
    print('# Atribute error, o atributo é privado')

# da pra fazer o acesso, mas não deveriamos fazer esse acesso
print(user._Acesso__senha)  # Name Mangling
# Em python ele nao te obriga a criar variaveis do tipo privadas
# da pra fazer acesso mesmo que vc coloque privado

# outra forma de ver é utilizando funções QUE ESTÃO DENTRO DA CLASSE, ai não tem nenhuma restrição

user.mostra_email()
user.mostra_senha()

"""
O que significa atributos de instancia?
Significa que ao criarmos instancias de uma classe, todas as instanciaa 
terão estes atributos
"""

user1 = Acesso('viviane@gmail.com', '223344')  # objeto/instancia da classe Acesso
user2 = Acesso('hulk@gmail.com', '741852')  # objeto/instancia da classe Acesso

user1.mostra_email()
user1.mostra_senha()
user2.mostra_email()
user2.mostra_senha()
print('\n')

# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------

# ATRIBUTOS DE CLASSE:

p1 = Produto('Playstation 4', 'Video Game', 4000)  # Criando produto com nome descrição e classe
p2 = Produto('Xbox ONE', 'Video Game', 2600)  # Criando produto com nome descrição e classe

"""
Atributos de classe, são atributos que são declarados diretamente na classe, ou seja,
fora do construtos, Geralmente já inicializamos um valor, e este valor é compartilhado entre
todas as instancias da class, Ou seja ao inves de cada instancia da classe ter seus proprios
valores como é o caso dos atributos de instancia, com os atributos de classe todas
as instancias terão o mesmo valor para este atributo.
"""

# REFATORANDO A CLASSE PRODUTO


class Produto:
    # atributo de classe
    imposto = 1.05  # equivale a 0.05% de imposto
    contador = 0  # atributo de classe contador, iniciado em 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1  # atributo de instancia. O produto vai receber o 0 + ele
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id  # aqui mostra o contador gerado, pois ali em cima fizemos a soma


produto1 = Produto('Playstation 4', 'Video Game', 4000)
produto2 = Produto('Xbox ONE', 'Video Game', 2600)

print(produto1.imposto)  # o valor é 1.05  // acesso possivel mas incorreto
print(produto2.imposto)  # o valor é 1.05 // acesso possivel mas incorreto

print(produto1.valor)  # o preço desse é 4000 e foi pra 4200 com imposto
print(produto2.valor)  # o preço desse é 2600 e foi pra 2730 com imposto

# OBS: Não precisamos criar uma instancia de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto)  # diretamente da classe da pra fazer // ACESSO CORRETO

print(f'a Id do playstation no sistema é: {produto1.id}')  # a id do produto 1 é 1
print(f'a Id do Xbox no sistema é: {produto2.id}')  # a id do produto 2 é 2

# fizemos uma logica pra que quando o produto for criado ele receba o valor do contador + 1

"""
OBS: Em linguagens como o java, os atributos conhecidos como atributos de classe
no python, em java são chamados de atributos estaticos;

OBS: Atributos de classe ocupam menos espaços alocados
exemplo, na classe Produto, se tivessemos 1000 objetos os atributos de classe
gastariam ainda apenas 2 espaços de memoria, enquanto os atributos de instancia seriam
4000
"""

# ATRIBUTOS DINAMICOS -
# É um atributo de instancia que pode ser criado em tempo de execução
# OBS: O atributo dinamico será exclusivo da instancia que o criou

produto3 = Produto('Bola de futebol', 'Esportes', 70.99)
produto4 = Produto('Notebook', 'Computadores e Acessorios', 3800)
print('\n')
# Criando um atributo dinamico em tempo de execução

produto3.peso = '5kg' # NOTE QUE NA CLASSE PRODUTO NÃO EXISTE O ATRIBUTO PESO

print(f'Produto: {produto3.nome}, Descrição: {produto3.descricao}, Valor: {produto3.valor}, Peso: {produto3.peso}')

try:
    print(f'Produto: {produto4.nome}, Descrição: {produto4.descricao}, Valor: {produto4.valor}, Peso: {produto4.peso}')
except AttributeError:
    print('O atributo peso foi criado apenas para instancia do produto 3, não existe para o 4')

# não é comum o uso de atributos dinamicos, é possivel mas não comum
print('\n')
# É POSSIVEL DELETAR ATRIBUTOS DINAMICAMENTE:

print(produto1.__dict__)  # dict mostra todas as informações de cada produto, devolve uma biblioteca
print(produto2.__dict__)  # dict mostra todas as informações de cada produto, devolve uma biblioteca
print(produto3.__dict__)  # dict mostra todas as informações de cada produto, devolve uma biblioteca
print(produto4.__dict__)  # dict mostra todas as informações de cada produto, devolve uma biblioteca

del produto3.peso
del produto4.descricao
del produto2.id
print('\n')
print(produto1.__dict__)
print(produto2.__dict__)
print(produto3.__dict__)
print(produto4.__dict__)