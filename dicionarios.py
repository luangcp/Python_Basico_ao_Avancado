"""
Dicionarios

OBS: Em algumas linguagens de programação os dicionarios python são conhecidos por mapas.

Dicionarios são coleções do tipo chave/valor.

Dicionarios são representados por chaves {}
sempre representado por {'oi': 'OLA'}

OBS:
- Chave e valor são separados por dois pontos 'chave:valor'
- Tanto chave quanto valor podem ser de qualquer tipo de dado;
- Podemos misturar tipos de dados;
"""
print(type({}))  # Classe dict de dicionario
print('\n')

# Criação de dicionarios
# Forma 1 (mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}  # 3 elementos nesse dicionario
print(paises)
print(type(paises))

# Forma 2 (menos comum)
paises1 = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')
print(paises1)
print(type(paises1))
print('\n')

# Acessando elementos

# Forma 1: Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['eua'])
# Caso tentamos fazer um acesso de uma chave que não existe da o erro KeyError

# Forma 2: Acessando via get (recomendado)

print(paises.get('br'))
print(paises.get('ru'))  # TIPO NONE
# Caso o get não encontre o objeto informado, será retornado o valor None e não será gerado KeyError
print('\n')

# --------------------------------------
# Exemplo não encontrando o país
pais = paises.get('ru', 'Não encontrado')  # Procura pra mim o ru se não achar manda o não encontrado
if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o pais')
# Exemplo encontrando o país
pais = paises.get('py', 'Não encontrado')  # Procura pra mim o py, se n achar manda o não encontrado
if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o pais')

print('\n')

# ------------------------------------------
# Sem o if e sem o else
pais = paises.get('ru', 'Não encontrado')

print(f'Encontrei o {pais}')

pais = paises.get('py', 'Não encontrado')

print(f'Encontrei o {pais}')
print('\n')

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada


# Verificando se uma chave se encontra nesse dicionario
print('br' in paises)
print('ru' in paises)
print('Estados unidos' in paises)
print('\n')

# Podemos utilizar qualquer tipo de dado ( int, float, string, boolean), inclusive
# listas, tupla dicionario, com chaves de dicionarios
localidades = {
    (35.6895, 39.6917): 'Escritorio em Tokio',
    (40.7128, 74.8060): 'Escritorio em Madrid',
    (35.7749, 39.4194): 'Escritorio no Brasil',
}
print(localidades)
print(type(localidades))
print('\n')

# Tupla é boa pra dicionarios pq é imutavel

# Adicionar elementos em um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 200}
print(receita)
print(type(receita))

# Forma 1: (mais comum)
receita['abr'] = 350
print(receita)

# Forma 2
novo_dado = {'mai':500}

receita.update(novo_dado) # Com update vc pode adicionar o dado ou atualizar
print(receita)
print('\n')

# Atualizando dados de um dicionario

# Forma 1:
receita['mai'] = 550
print(receita)

# Forma 2

receita.update({'mai': 600})
print(receita)

# Conclusão: a forma de adicionar novos elementos ou atualizar dados em um dicionario é a mesma
# Conclusão: Em dicionarios, NÃO, podemos ter chaves repetidas
print('\n')

# Remover dados de um dicionario
# Forma 1:
ret = receita.pop('mar')  # pop é pra remover o ultimo elemento da lista
print(ret)
print(receita)

# OBS: aqui tem que sempre informar a chave, caso não encontre o elemento da keyerro
# OBS: ao removermos um objeto, o valor desse objeto é SEMPRE retornado
print('\n')

# Forma 2:
del receita['fev']  # Nesse caso o valor removido não é retornado
print(receita)
print('\n')

# Imagine que você tem um comercio eletronico, onde tem um carrinho eletronico na qual adicionamos produtos.
"""
Carrinho de compras:
    Produto 1:
        - Nome
        - Quantidade 
        -Preço
    Produto 2:
        - Nome
        - Quantidade 
        - Preço

Poderiamos utilizar uma lista para isso? SIM
"""
# 1- Poderiamos utilizar uma lista para isso? SIM

carrinho = []

produto1 = ['Playstation 4', 1, 2000]
produto2 = ['Bola de futebol', 1, 70.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
print('\n')

# Teriamos que saber qual é o indice de cada informação no produto

# Forma 2 - Poderiamos usar um tupla para isso? SIM
produto1 = ('Playstation 4', 1, 2000)
produto2 = ('Bola de futebol', 1, 70.00)

carrinho = (produto1, produto2)
print(carrinho)
# Teriamos que saber qual é o indice de cada informação no produto
print('\n')

# Poderiamos utilizar um dicionario para isso? SIM
carrinho = []
produto1 = {'nome': 'Playstation 4', 'Quantidade': 1, 'Preço': 2000}
produto2 = {'nome': 'Bola', 'Quantidade': 1, 'Preço': 75.50}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
# Dessa forma facilmente add ou removemos produtos no carrinho, e em cada produto
# Podemos ter certeza sobre cada informação

print('\n')

# Metodos de dicionarios:

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionario (zerar dados)
d.clear()
print(d)

# Copiando um dicionario para outro
d = dict(a=10, b=25, c=32)
novo = d.copy()  # Deep copy
print(novo)

novo['d'] = 4

print(d)
print(novo)
print('\n')

# Forma 2: Shallow copy (os dois sofrem alteração)
d = dict(a=1, b=2, c=3)
novo = d
print(novo)

novo['d'] = 4
print(d)
print(novo)
print('\n')

# ----------------------------------------------

# Forma não usual de criação de dicionarios

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

print('\n')

usuarios = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuarios)
print(type(usuarios))

# OBS: o metodo fromkeys: recebe dois parametros: um iteravel e um valor.
# Ele vai gerar para cada valor do iteravel uma chave e irá atribuir a esta chave o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 10), 'novo')
print(veja)