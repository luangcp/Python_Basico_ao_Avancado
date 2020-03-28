"""
Dunder Name e Dunder Main

Dunder -> Doble Under

Dunder Name -> __name__

Dunder Main -> __main__

Em python são utilizados Dunder para criar:
funções/atributos/propriedades e etc utilizando Double Under
para nao gerar conflito com os nomes desses elementos na programação

# Na linguagem C, temos um programa da seguinte forma:

int main(){

    return 0;
}

# Na linguagem java, temos um programa da seguinte forma:

public static void main(String[] args) {
}

 - EM PYTHON, Se executarmos um modulo python diretamente na linha do comando,
 internamente o python atribuira a variaval __name__ o valor __main__
 indicando que este modulo é o modulo de execução principal

Main -> Significa principal

"""
from funcao_soma_impares import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7]))


# Funções não devem printar nada só se for main


# Utilizando os python files: primeiro.py e segundo.py

import primeiro
import segundo

# CONFUSO

