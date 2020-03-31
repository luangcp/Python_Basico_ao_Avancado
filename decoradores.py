"""
DECORADORES -- Decorators

O que são decorators?

- Decorators são funções:
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem um sintaxe propria, usando '@' (syntact sugar / açucar sintatico)

|----------------------------------------------\
|              Function Decorator              \
------------------------------------------------

-------------------------------------------------
|-----------------------------------------------\
|            Função    decorada                 \  # APRIMORADA, DECORADA DE DECORAR DEIXAR BONITO
|-----------------------------------------------\
-------------------------------------------------
"""

# Decorators com funções ( Sintaxe nao recomendada / Sem açucar sintatico)


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhece-lo')
        funcao()
        print('Tenha um otimo dia!')
    return sendo


def saudacao():  # Função aprimorada
    print('Seja bem-vindo')


# TESTANDO 1
teste = seja_educado(saudacao)  # APRIMORANDO O COMPORTAMENTO DA FUNÇÃO SAUDAÇÃO

teste()

print('\n')
# TESTANDO 2


def raiva():
    print('EU TE ODEIO! ')


raiva_educada = seja_educado(raiva)

raiva_educada()

# --------------------------------------------------------------------
print('\n')
# Decorators com Syntax Sugar (Açucar Sintático)


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um excelente dia')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Luan')


print('\n')
# Testando
apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir...')

dormir()
print('\n')

# EXEMPLO EM SITES/WEBSITES

# imagine que abaixo seja um site

"""
| --------------------------------------------------------------------
|   Home        |   Serviços     |   Produtos   |  Administrativos   |
----------------------------------------------------------------------

em que vc clique em home vai pra home, serviços pra serviços, mas apenas
usuarios com permissão vão em administrativo

http://www.meusite.com.br/home

http://www.meusite.com.br/servicos

http://www.meusite.com.br/produtos

http://www.meusite.com.br/admin  # QUEREMOS RESTRINGIR O ACESSO A ELA

OBS: NÃO É CODIGO FUNCIONAL, É APENAS EXEMPLO

def checa_login():
    id not request.usuario:
        redirect('http://www.meusite.com.br')
    
def home(request):
    return 'Pode acessar home'
    
def servicos(request):
    return 'Pode acessar servicos'
    
def produtos(request):
    return 'Pode acessar produtos'

@checa_login  # Funçao decorada -- a partir do momento que decoramos, quando alguem tentar o acesso, sera carregada essa
def admin(request):
    return 'Pode acessar admin'
"""

# OBS: Não confunnda decoration com decoretor function
# Decoretor é o @blablabla e o decoretion function é a propria função decoradora