"""
Instalando e utilizando modulos externos

Em python para instalar modulos ou pacotes externos que não fazem parte da biblioteca
padrao da linguagem é utilizado o gerenciador de pacotes python chamado: Pip
Pip - Python Installer Packege

Voce pode conhecer tds os pacotes externos oficiais em: https://pypi.org

Instalando um novo pacote: Colorama

é utilizado para permitir impressão de texto coloridos no terminal

entrar no terminal e digitar: pip install colorama

Para instalar modulo:
pip install nome_do_modulo

* Mas lembrando que é so entrar no site e ver

# Importando arquivo pdf com python
install -> pip install python-pdf
"""
"""
# Exemplo colorama

from colorama import init, Fore

init()

print(Fore.LIGHTBLUE_EX + 'Luan Gabriel Cardoso Pinheiro')
print(Fore.RED + 'Estudante de Engenharia de Controle e Automação')
print(Fore.MAGENTA + 'No Instituto Federal de Educação Ciência e Tecnologia')
"""
# Python Geração de PDF

import pydf

pdf = pydf.generate_pdf('<h1> luan </h1>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
