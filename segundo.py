# -*- coding: UTF-8 -*-

import primeiro


def funcao2():
    primeiro.funcao1()


if __name__=='__main__':
    print('segundo.py está sendo executado diretamente.')
else:
    print(f'segundo.py foi importado. {__name__}')