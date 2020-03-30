"""
Escrevendo um Iterador customizado

Para criar um iterador customizado basta ter __iter__ e __next__
"""
# Orientação a objetos:
# Funções dentro de uma classe são chamados de metodos
# função __init__ (self,menor,maior)  = função construtor
# self = sempre vai ver quando for uma função dentro de uma classe


class Contador:  # Declarando uma classe
    def __init__(self, menor, maior):  # Metodos
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


con = Contador(1, 6)

print(con)
print(con.menor)
print(con.maior)

# Transformando esse con num iteravel
# Precisa de um outro metodo especial

it = iter(con)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))  # STOP ITERATION

# Tambem podemos fazer:

for n in Contador(1, 61):
    print(n)


# Fazendo em range:

for n in range(1, 61):
    print(n)