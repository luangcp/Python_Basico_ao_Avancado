"""
Modulo Collections Deque

Podemos dizer que o deque é uma lista de alta perfomace.


"""
# -*- coding: UTF-8 -*-
# Import
from collections import deque

# Criando deques

deq = deque('Luan')
print(deq)
# Ele pegou a string e separou cada uma delas fazendo uma lista de strings

# Adicionando elementos no deque
deq.append('y')
print(deq)

deq.appendleft('k')  # Adiciona um elemento no começo da lista
print(deq)

# Remover elementos
print(deq.pop())  # Remove ou recoloca além de retornar o item do final
print(deq)
print(deq.popleft())  # Remove ou recoloca além de retornar o item inicial
print(deq)
