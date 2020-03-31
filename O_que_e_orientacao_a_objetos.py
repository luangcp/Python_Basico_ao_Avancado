"""
ORIENTAÇÃO A OBJETOS

O que é orientação a objetos -> é um paradigma de programação
que utiliza que mapeamento de objetos do mundo real para
modelos computacionais

PARADIGMAS DE PROGRAMAÇÃO: Forma de desenvolvimento do software
como vc vai pensar pra desenvolver o software
Programação estruturda, orientação a objetos, funcional
Depende muito da linguagem que você está utilizando
* exemplo: a linguagem c não tem orientação a objetos
* a linguagem java por outro lado está dentro da orientação ao objetos
* o python já e multiparadigma, comporta todos os tipos

A programação orientada a objetos:
- O objetivo é mapear algo do real para o computacional
para que podemos representar suas caracteristicas e desenvolvimento

PRINCIPAIS ELEMENTOS:

Classe = modelo do objeto no mundo real sendo representado computacionalmente
exemplo: produto

Atributos: caracteristicas do objeto
uma classe pode ter nenhum ou varios atributos
exemplo: nome do produto, preço do produto, e desconto

Metodos: Comportamento do objeto - (entenda metodos como funções)
o metodo está dentro de uma classe

Construtor: é um metodo especial, utilizado pra criar os objetos a partir de uma classe
ex: Notebook preço 2300 com 15% de desconto // caneta bic preço 2,94 com 5% de desconto

Objeto: elementos que criamos atraves das classes ou instancias || instancia da classe


"""
# exemplo
numero = 10
print(numero)
print(type(numero))

nome = 'Luan'
print(nome)
print(type(nome))


class Produto:  # Construtor
    pass


ps4 = Produto()  # criei um produto chamado ps3 utilizando o construtor acima
print(ps4)  # mostra onde foi alocado em memoria
print(type(ps4))  # vai mostrar que a classe dele é produto
# basicamente vamos criar o tipo de software que quisermos
