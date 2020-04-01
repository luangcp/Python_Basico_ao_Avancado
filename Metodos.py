"""
POO - Métodos
Metodos -> (funções), representam o comportamento do objeto, ou seja as ações
que este objeto pode realizar no seu sistema.

Em python dividimos os metodos, em 2 grupos: Metodos de instancia e metodo de classe.


# LEMBRANDO QUE O METODO __init__ é o construtor

O metodo dunder init __init__ é um metodo especial chamado de construtor e
sua função é construir o objeto a partir da classe

OBS: Todo elemento em python que inicia e finaliza com duplo underline *Double Underline*
é chamado de dunder

OBS: Os metodos dunder em python são chamados de metodos magicos

ATENÇÃO: Por mais que possamos criar nossas proprias funções utilizando dunder no inicio e no fim
não é aconselhado, pois pode ser que entre em conflito com funções do python, mudando o comportamento
então é melhor que nunca se faça metodos dessa maneita

# Metodos são escritos em letras minusculas. Se o nome for composto por dois nomes
eles seram separados por underline

# Metodos de classe em python sao conhecidos como metodos estaticos em outras linguagens

"""
# Metodos de instância


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:
    contador = 2305  # A primeira conta criada, vai ser 2305, dps 2305 +1

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id
    # criando metodo

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""  # docstring
        return (self.__valor * (100 - porcentagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp  # biblioteca pra criptografar senha


class Usuario:

    contador = 0

    @classmethod  # decorator . tem acesso a classe
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuarios no sistema')

    @staticmethod  # METODO ESTATICO não tem acesso a classe nem acesso a instancia
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__sobrenome = sobrenome
        self.__nome = nome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=20000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    def __correr__(self, metros):
        print(f'{self.__nome}Estou correndo {metros} metros')
        # usar metodos com a mesma grafia do python reservada pode acarretar em problemas

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]



# EXEMPLOS DE UTILIZAÇÃO
# Exemplo 1 - desconto em produto utilizando a class Produto e o metodo desconto

produto1 = Produto('Playstation 4', 'Video Game', 2800)
print(f'O valor com o desconto é {produto1.desconto(20)}')

# Exemplo 2 - Utiizando classe Usuario
usuario1 = Usuario('Luan', 'Pinheiro', 'luan@gmail.com', '123')
usuario2 = Usuario('Viviane', 'Mozelli', 'vivi@gmail.com', '123')

print(usuario1.nome_completo())

print(Usuario.nome_completo(usuario1))

print(usuario2.nome_completo())

# CRIPTOGRAFANDO A SENHA

# utilizar a biblioteca from passlib.hash import pbkdf2_sha256 as cryp

nome = input('Informe o nome')
sobrenome = input('Informe o sobrenome')
email = input('Informe o email')
senha = input('Informe o senha')
confirma_senha = input('Confirme a senha:')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere..')
    exit(42)


print('Usuario criado com sucesso!')

senha = input('Informe a senha para acesso')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha user criptografada: {user._Usuario__senha}')

# ---------------------------------------------------------------
# Metodos de classe

# utilizamos decorators

usuario3 = Usuario('Hulk', 'Meu filho', 'hulk@gmail.com', '123456')

Usuario.conta_usuarios()  # Forma correta via nome de classe
usuario3.conta_usuarios()  # Possivel mas incorreto via instancia de classe

# METODOS PRIVADOS

# sao feitos com __ antes


"""
def __gera_usuario(self):
    return self.__email.split('@')[0]
"""

teste = Usuario('francisco','Peixe','francisco@gmai.com','123')

try:
    print(teste.__gera_usuario())
except AttributeError:
    print('é privado faça dessa maneira para ler: _Usuario__gera_usuario')

print(f'O nome de usuario automatico criado foi: {teste._Usuario__gera_usuario()}')

# METODO ESTATICO
# Também utiliza decorador

print(Usuario.contador)
print(Usuario.definicao())

teste2 = Usuario('stela','coelha','stela@gmai.com','123')

print(teste2.contador)

print(teste2.definicao())
