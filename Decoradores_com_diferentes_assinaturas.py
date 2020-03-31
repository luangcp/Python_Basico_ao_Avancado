"""
Decorators com diferentes assinaturas

A assinatura de uma função é representada pelo seu retorno, nome e parametros de entrada.

funções decoradoras com diferentes parametros de entrada
"""

# RELEMBRANDO


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()  # função upper deixa td maisculo
    return aumentar


@gritar  # aplicando decorator
def saudacao(nome):
    return f'ola eu sou o {nome}'


# Função para pedir um prato e o acompanhamento

@gritar
def ordenar(principal, acompanhamento):
    return f'olha eu gostaria de {principal}, acompanhado de{acompanhamento}'


# Testando

print(saudacao('Luan'))  # Ate agora executando somente a saudação
# O decorator basicamente coloca uma função menor dentro de uma completa
# No exemplo acima uma função de receber nome entrou dentro de uma pra transformat td em caiza alta

# Agora o exemplo com o de ordenar dos pedidos
try:
    print(ordenar('Picanha', "Batata-Frita"))  # estamos enviando 2 parametros para uma função de um só
except TypeError:
    print('Era esperado apenas uma entrada e você mandou mais de uma \n'
          'Por favor veja o proximo exemplo corrigindo com Decorator Pattern')

# Para resolver utilizamos um padrão de projeto chamado decorator pattern
print('\n')
# REFATORANDO COM A DECORATOR PATTER


def gritar1(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()  # função upper deixa td maisculo
    return aumentar


@gritar1
def ordenar1(principal, acompanhamento):
    return f'Ola eu gostaria de {principal} acompanhado de {acompanhamento} por favor'


print(ordenar1('Picanha', "Batata-Frita"))

# A assinatura de uma função é representada pelo seu retorno, nome e parametros de entrada.

print('\n')

# OBS: Vale lembrar que podemos utilizar parametros nomeados

print(ordenar1(acompanhamento='Batata', principal='Picanha'))

print('\n')

# Decorators com argumentos
# Com parametros de entrada


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Pimeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')  # o primeito sempre tem que ser pizza
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


# TESTANDO

print(soma_dez(10, 12))  # O PRIMEIRO ARGUMENTO OBRIGATORIAMENTE TEM QUE SER DEZ
print(soma_dez(1, 21))

print(comida_favorita('pizza', 'churrasco'))  # OK
print(comida_favorita('hamburguer', 'pudim'))  # vai dar errado pq o primeiro tem q ser pizza

