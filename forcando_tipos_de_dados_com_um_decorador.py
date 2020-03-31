"""
Forçando tipos de dados com um decorador

fazendo uma aplicação pratica com objetivo
"""
# antes só relembrar o comando zip:
a = (1, 2, 3)
b = (2, 4, 6)

c = zip(a, b)
print(c)


def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):  # Com zip pegamos e juntamos os primeiros de cada, segundo de cada
                novo_args.append(tipo(valor))  # str('luan'), int('4')
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


# TESTANDO

repete_msg('Luan', '4')


@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)


dividir('1', 5)
