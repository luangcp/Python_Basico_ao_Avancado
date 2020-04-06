"""
Alocação e gerencia de memoria em python

em python tudo é objeto, seja do tipo inteiro, do tipo string, classe

COMPARANDO PYTHON E OUTRAS LINGUAGENS COMO JAVA e C

DECLARAÇÃO                  PYTHON                                 JACA/C
declaração                    x=10                                int x = 10;
declaração de tipo         n necessario                           Obrigatorio
o que é 10?           um objeto criado na memoria heap         um dado primitivo armazenado em 4 bytes
O que x contem?            referencia para o objeto 10             local de memoria onde 10 é armazenado
x = x+1               x é referenciado a um novo objeto           x continua apontando pro msm local de memoria



- Metodos e variaveis são criadas na memoria stack;
- Os objetos e instancias são criadas na memoria heap;
- Um novo stack é criado durante a invocação de uma função ou metodo;
- Stacks são destruidas sempre que uma função ou metodo retorna valor
- Garbage collector é um mecanismo para limpar dead objects;


"""