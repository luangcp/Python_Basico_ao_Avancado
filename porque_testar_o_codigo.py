"""
Porque testar nosso codigo?

Teste automatizados!

Aplicação we possue duas partes
---------------------------------------------
|                                            |
|             frontend  e backed             |
----------------------------------------------
|             Testes automatizados           |
----------------------------------------------
Testes automatizados: verificando tudo de forma automatica, testes criado por desenvolvedores para
ver se tudo ta ok

Testes em softwares são polemicos pq td mundo sabe que é importante, mas nem td mundo faz
pq tem que escrever mais codigos

frontend -> visõa que o usuario vai ver
backend -> o que rola por trás, um banco de dados formatados para serem renderizados no frontend


Porque testar nosso codigo:
    - Reduzem bugs (problemas) no código existente;
    - Testes garantem que novos recursos da sua aplicação não quebrem (alterem) recursos antigos;
    - Testes garantem que bugs (problemas) que forem corrigidos anteriormente continuem corrigidos;
    - Testes garante que a refatoração não traga novosvos bugs (prblemas)

Porque algumas pessoas não gostam:
    - Os testes tornam o processo mais lento
    - Tornam o desenvolvimento chato
    - As vezes temos que escrever mais teste do que o proprio cofigo

TDD - Test Driven Development (Desenvolvimento Guiado por testes)
- O teste é criado ante mesmo do codigo

Com TDD São utilizaos estagios de desenvolvimento:
    - Você escreve seu teste primeiro;
    - Então você escreve o codigo minimo suficiente para fazer o teste passar
    - Então refatora o código para realizar a funcionalidade e testa novamente
    - Uma vez que o teste passe, o recurso é considerado completo;

Estes estágios de desenvolvimento do TDD São quase como um mantra que os desenvolvedores seguem, conhecidos como:
    - Red;  ->  o teste vai falhar
    - Green;  -> quando o teste passa  -> escreve um codigo minimo necessario para o teste passar
    - Refactor;  -> refatorar
"""


class Cachorro:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def latir(self):
        print(f'{self.__nome} esta latindo')


hulk = Cachorro('Hulk')
hulk.latir()
print(hulk.nome)