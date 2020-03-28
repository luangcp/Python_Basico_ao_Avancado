"""
Recebendo dados do usuario

input() ->  Todo dado recebido via input é do tipo String

Em python, string é tudo que estiver entre:
- Aspas simples;
- Asplas duplas;
- Asplas simples triplas;
- Asplas duplas triplas;

Exemplos:
-Aspas simples -> 'Luan'
- Aspas duplas -> "Luan"
assim mesmo pra triplas
"""
# -*- coding: UTF-8 -*-
# Entrada de dados
print('Qual o seu nome?')
nome = input()

# Exemplo de print antigo
print('Seja bem-vindo(a) %s' % nome)  # o % s substitui o valor na variavel

# Exemplo de print atual
print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print mais atual de todos
print(f'Seja bem vindo(a) {nome}')


print('Qual a sua idade?')
idade = input()

# Processamento


# Saída de dados

# Um tipo de print pra saida
print('A', nome, 'Tem', idade, 'Anos')

# Outro tipo
print(f'A {nome} Tem {idade} anos')  # Prefiro assim particulamente

# Outro tipo
# int(idade) => cast
# Cast é a converção de um tipo de dado para outro
# Possivel realizar calculos
print(f'A {nome} nasceu em {2020 - int(idade)}')

# Outra forma
nome = input('Qual o seu nome \n')

idade = int(input('Qual sua idade \n'))

print(f'A {nome} nasceu em {2020 - int(idade)}')
