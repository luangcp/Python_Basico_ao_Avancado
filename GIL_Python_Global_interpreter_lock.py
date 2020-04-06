"""
O python global interpreter lock -> é um mutex (ou lock) que permite aprenas uma
thread tome conta do interpretador
"""

import time
from threading import Thread

CONTADOR = 50000000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


inicio = time.time()
contagem_regressiva(CONTADOR)
fim = time.time()

print(f'O tempo em segundos {fim - inicio}')