"""
Definindo funções

- Funções são pequenas partes de código que realizam tarefas especificas:
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes

OBS: Se você escrever um função que realize varias tarefas dentro dela,
é bom fazer uma verificação para que a função seja simplificada

Já utilizamos varias funções desde que iniciamos esse curso:
- print()
- len()
- max()
- min()
- count()
- e muitas outras.


"""
# Exemplo de utilização de função

# cores = ['verde', 'amarelo', 'vermelho', 'preto', 'azul', 'rosa']

# Utilizando a função integrada (Built-in) do python print()
# print(cores)

# curso = 'Programação em python: essencial'
# print(curso)

# cores.append('roxo')  # Só usa append com lista

# ---------------------------------------------------------------
# Principio DRY - Don't repeat yourself - Não repita vc mesmo/não repita seu codigo

"""
Em python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada)
    bloco_da_funcao

onde:
nome_da_funcao -> SEMPRE, com letras minusculas, e se for composto separado por underline
parametros_de_entrada -> opcionais, onde tendo mais de um, cada um separado por virgula, opcionais ou não
bloco_da_funcao -> Também chamado de corpo da função ou implementação, onde o processamento acontece
Neste bloco, pode ter ou não retorno da função

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def'
informando ao python que estamos definindo uma função. Também abrimos o bloco de codigo
com o já conhecido dois pontos ':' que é utilizado em python para definir blocos


"""
# Definindo a primeira função
# Definição:


def diz_oi():
    print('oi')


"""
OBS: Veja que, dentro das nossas funções podems utilizar outras funções
2 - veja que nossa função só executa 1 tarefa, ou seja, a unica coisa que ela faz
é dizer oi:
3- Veja que esta função não recebe nenhum parametro de entrada.
4- veja que essa função n retorna nada
"""

# Utilizando funções

# Chamada de execução
diz_oi()  # É necessario abrir e fechar os parenteses


# Exemplo 2:


def cantar_parabens():
    print('Parabens pra voce')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!!')


# Executando a função
cantar_parabens()


# Exemplo em um loop usando range para cantar 5 vezes
for n in range(5):
    cantar_parabens()

# Em python podemos inclusive criar variaveis do tipo de uma função e executar esta função através da variavel
canta = cantar_parabens
print('Variavel canta:')
canta()
