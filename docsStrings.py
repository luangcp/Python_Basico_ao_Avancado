"""
Documentando funções com DocsStrings

OBS: Podemos ter acesso á documentação de uma função em Python
utilizando a propriedade especial __doc__

Podemos ainda fazer acesso a documentação com a função help()

"""

print(help(print))


# Exemplos
def diz_oi():
    """ Uma função simples que retorna a string 'oi!' """  #docstring
    return 'Oi!'


print(diz_oi())

print(help(diz_oi))

print(diz_oi.__doc__)

print('\n')




def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão e o quadrado de 'numero' ou 'numero' á 'potencia' informada.
    :param numero: numero que desejamos gerar o exponencial.
    :param potencia: Potencia que queremos gerar o exponencial. Por padrão é 2
    :return: Retorna o exponencial de 'numero' por 'potencia'.
    """
    return numero ** potencia


print(exponencial)

print(help(exponencial))

print(exponencial.__doc__)


