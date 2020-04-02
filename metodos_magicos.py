"""
POO - Metodos magicos

Métodos magicos são todos os metodos que utilizam dunder __  __

dunder init -> __init__

Dunder > douber underscore

OUTROS:
# __rapr__ -> representação do objeto

# __str__ -> outro metodo de representação, com strings, tem prioridade

# __len__ -> utilizado para olhar tamanho, saber tamanho de algo, no exemplo abaixo vendo o numero de paginas do livro

# __del__ -> deletando algo

# __add__ -> somando algo, recebendo 2 objetos

# __mul__ -> multiplicação



"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):  # sobrescrevendo o endereço de memoria padrão
        return self.titulo

    def __str__(self):  # sobrescrevendo o endereço com uma string
        return self.titulo

    def __len__(self):  # definindo que o len vai ser o numeros de paginas do livro. len = tamanho
        return self.paginas

    def __del__(self):  # Deletando
        print('Um objeto do tipo Livro foi deletado da memoria')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('Mundo dos cachorros!', 'Hulk escritor', 500)
livro2 = Livro('Inteligencia artificial!', 'Luan', 350)

print(livro1)  # endereço de memoria dos objetos
print(livro2)  # endereço de memoria dos objetos

print(len(livro1))  # quantidade de pagina livro 1
print(len(livro2))  # quantidade de pagina livro 2

print(livro1 + livro2)  # juntando o nome dos livros

print(livro1 * 4)  # titulo do livro * 4
print(livro2 * 2)  # titulo do livro * 2
print(livro1 * 'luan')  # não pode multiplicar