"""
COMO CRIAR VARIAVEIS DE AMBIENTE

Primeiro:
ir em:
 - meu computador
 - Disco local C
 - usuarios : entra no usuario que deseja
 - entrar no AppData  ->  C:\Users\luang\AppData
 - Local
 - Programs
 - Python
 - Versão mais recente do python
 - Scripts
 - copiar o enderenço -> C:\Users\luang\AppData\Local\Programs\Python\Python38-32\Scripts

Segundo:
 - Ir no painel de controle
 - Sistema e segurança
 - Sistema
 - Configurações avançadas do sistema
 - Variaveis de ambiente
 - Vai em path e clica em editar
 - Clica em novo e cola o endereço -> C:\Users\luang\AppData\Local\Programs\Python\Python38-32\Scripts
 - Da ok
 - Clica em novo (em variaveis do sistema)
 - Variavel name: WORKON_HOME
 - Variavel value: %USERPROFILE%\Envs

 Terceiro:
  - Abre o cmd
  - pip  install virtualenv
  - pip instal virtualenvwrapper-win
  - fecha e abre o cmd dnv
  - mkvirtualenv nome_da_variavel_de_amiente
  - PRONTO
"""