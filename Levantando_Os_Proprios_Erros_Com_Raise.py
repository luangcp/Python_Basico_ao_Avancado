"""
Levantando os proprios erros com raise

raise -> Lança exceções

OBS: O raise não é uma função. é uma palvra reserada, assim como def ou qualquer outra em python

Para simplificar, pense no raise como sendo util para que possamos criar nossas
proprias exceções e mensagens de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de Erro')

OBS: O raise, assim como o return, finaliza a função, ou seja, nada apos ele é executado
"""

# Exemplo:


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:  # Verifica se o texto é uma string, se nao for exceção
        raise TypeError('Texto precisa ser uma String')
    if type(cor) is not str:  # Verifica se cor é uma string, se não for exceção
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:  # Verifica se a cor escrita esta contida em cores, se n for exceção
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Luan', 'lilas')
colore(8, 'Verde')  # Erro
colore('Luan', 8)  # Erro
