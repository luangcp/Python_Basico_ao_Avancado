
def funcao1():
    print('Luan Pinheiro . primeiro.py')


if __name__=='__main__':
    funcao1()
    print('primeiro.py está sendo executado diretamente')
else:
    print(f'Primeiro.py foi importado. {__name__}')