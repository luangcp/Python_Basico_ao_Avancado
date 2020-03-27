"""
Erros mais comuns em Python

ATENÇÃO:
É importante prestar atenção e aprender a ler as saídas de erro

usar printf ao inves de print -> NameError: name 'printf' is not defined

Erros mais comuns:

SyntaxError -> Ocorre quando o python encontra o erro de sintaxe. Ou seja, você
escreveu algo que o python não reconhece como partes da linguagem.

Exemplos SyntaxError

a)
def funcao:                   # A definição de função é feita com ()
    print('Luan Pinheiro')

b)
None = 1  -> Não pode pois none é uma palavra reservada do python
def = 1

c)

return  -> não pode colocar o return sozinho, ele precisa retornar algo

2 - NameError -> Ocorre quando uma variavel ou função não foi definida

Exemplos NameError:

a)
print(geek)  -> NameError pois geek nao estava definido antes

b)
a = 8
if a < 10:                         -> msg nao foi definido antes, ent se o valor for maior que 10 da erro
    msg = 'é maior que 10'
print(msg)

3 - TypeError - Ocorre quando uma função/operação/função é aplicada a um tipo errado.

Exemplos TypeError:

a)print(len(5))  -> TypeError: object of type 'int' has no len()

b) print('Luan' + [])  -> TypeError: não pode uma lista + uma string

4- IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo
de dado indexado utilizando um indice invalido.

Exemplo IndexError

a) lista =['geek']          -> IndexError: string index out of range
print(lista[0][10])          -> nao tem a posição 10


5 - ValueError -> Ocorre quando uma função/operação built-in (integrada)
recebe um argumento com tipo correto mas valor inapropriado

exemplos valueerror:

a) print(int('Luan')  -> não da pra converter luan pra int

6 - KeyError -> Ocorre quando tentamos acessar um dicionario com uma chave
que não existe

Exemplos KeyError:

a) dic = {}           -> não tem luan no dicionario
print(dic['luan']

7 - AttibuteError -> Ocorre quando uma variavel, não tem um atributo ou função

Exemplos AtributeError

a) tupla = (11, 2, 3, 44)  -> Nao tem esse atributo para tupla
print(tupla.sort())

8 - IndentetionError -> Ocorre quando não respeitamos a identação do python que é de 4 espaços

a)
def nova()   -> Não teve a indentaçao ent nao da
print('Luan')

b) if f > 20:  - Vai dar erro de identação tbm
print('oi')

OBS: Exceptions e erros são sinonimos na programação

OBS: Importante ler e prestar atenção na saída de erro.
"""
lista =['geek']
print(lista[0][10])