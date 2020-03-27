"""
Escopo de variaveis

Dois casos de escopo:
1- Variaveis Globais:
   - Variaveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.
2- Variaveis Locais:
   - Variaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
   está limitado ao bloco onde foi declarado

Para declarar variaveis em python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinamica. Isso significa que ao declararmos uma variavel
nos não colocamos o tipo de dado dela.
esse tipo é indeferido ao itriburimos valor à mesma

exempllo em C:
int numero =42;

Exemplo em Java:
int numero =24;
"""

numero = 42  # Exemplo de variavel global
print(numero)
print(type(numero))

numero = 'Luan'
print(numero)
print(type(numero))

nao_existo = 'Oi'
print(nao_existo)

numero = 42
novo = 0
if numero > 10:
    numero = numero + 10  # A variavel 'novo' está declarada localmente dentro do bloco if. Portanto é local
    print(novo)

print(novo)