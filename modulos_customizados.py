"""
Modulos Customizados - Modulos criados por nós mesmos

Todos arquivos que vc ja criou ou já fez é um modulo python e pode ser reaproveitado ou reutilizado

Como modulos python nada mais são do que arquivos python, então todos os arquivos
criados são modulos Python prontos para serem utilizados

"""
# Importando uma função especifica do modulo
from funcoes_com_parametro import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 23, 14]))

# importando todo o modulo (temos acesso a todos os elementos do modulo)
import funcoes_com_parametro as fcp

# Estamos acessando e imprimindo uma variavel contida no módulo
print(fcp.lista)

print(fcp.soma_impares(fcp.lista))
print('\n')

# Outro
from map import cidades, c_para_f

print(list(map(c_para_f, cidades)))
