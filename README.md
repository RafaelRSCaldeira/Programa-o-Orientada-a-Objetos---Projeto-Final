# Projeto Final da disciplina Programação Orientada a Objetos, ministrada em 2024.1

REGRAS PARA TODOS OS GRUPOS:
Variáveis, métodos e nome de classes em INGLÊS.
Usaremos o camelCase, exceto para nome de classes, que será PascalCase.
Código CLARO e LIMPO, ou seja, nome de variáveis e métodos descritivos. É preferível utilizar um nome grande e descritivo do que pequeno e confuso. Evitem de criar variáveis com número ou com apenas uma letra. Mais detalhes sobre código limpo ao final do documento. 
O código deverá conter TYPE HINTS em todos os métodos implementados, indicando o tipo da variável e o tipo de retorno da função.

Banco de dados: 
Tabela usuários: ID (PK), NAME, EMAIL, PASSWORD, POSITION.
Tabela clientes: ID (PK), NAME, EMAIL, COMPANY, PHONE
Tabela problemas: ID (PK), DESCRIPTION, SLA
Tabela chamados: ID (PK), TITLE, DESCRIPTION, CATEGORY, CLIENT_ID (FK), USER_ID (FK), STATUS, OPENING_DATE, MAX_DATE, CLOSING_DATE.
Deverá ser feita uma interface de acesso ao banco de dados e quatro classes que implementam a interface, uma para cada tabela. Elas deverão seguir o padrão de projeto Singleton, logo só poderá existir uma instância de cada classe. A interface deverá possuir os métodos: create, insert, searchByID, searchAll, update e delete.

Interface Gráfica:
Desenvolver a interface gráfica utilizando a biblioteca Tkinter. 
Criar as telas de login, de gerenciamento de chamados, usuários, clientes e categorias de problemas. 
Implementar a autenticação de usuários e redirecionamento pós-login.


Gerenciamento de Usuários e Clientes:
Criar as classes Person, Client e User.
Person (classe abstrata): 
•	Atributos: id, name, email.
•	Métodos: register, view, update, delete (todos abstratos).
Client (herda Person):
•	Novos atributos: company, phone.
User (herda Person):
•	Novos atributos: password, position.
Utilizaremos a classe abstrata Person, pois as classes Client e User compartilham de alguns atributos e métodos com o mesmo nome. Além disso, o uso de uma classe abstrata permite que as classes sejam mais flexíveis, podendo, em casos específicos, usar as ambas as classes de forma intercambiável.
Todos os métodos, exceto view, usarão as classes disponibilizadas pelo grupo 5 (Banco de Dados) para acessar o banco de dados. 


Gerenciamento de Chamados:
Criar a classe Ticket.
Ticket:
•	Atributos: id, title, description, category, client_id, user_id, status, opening_date, max_date, closing_date. 
•	Métodos: open, assignUser, changeStatus, close, view, update, delete
Todos os métodos, exceto view, irão interagir com o banco de dados através das classes fornecidas pelo grupo 5 (Banco de Dados).
Desenvolver uma interface para listar os chamados baseados em seu status, com todas as datas relevantes.


Categorias de Problemas e SLAs:
Criar a classe Problem.
Problem:
•	Atributos: id, description, sla
•	Métodos: registe, view, update, delete
Todos os métodos, exceto view, irão interagir com o banco de dados através das classes fornecidas pelo grupo 5 (Banco de Dados).
 
Código limpo é um conceito na engenharia de software que se refere à prática de escrever código de forma que seja fácil de entender e manter. Um código limpo é bem organizado, claro, conciso e segue padrões de codificação consistentes. Ele é fácil de ler e compreender, facilitando o trabalho de outros desenvolvedores que possam precisar entender, modificar ou dar manutenção ao código no futuro.
Alguns princípios comuns de código limpo incluem:
Clareza: O código deve ser fácil de entender, com nomes significativos para variáveis, funções e classes. Comentários devem ser usados para explicar partes complexas ou pouco claras do código.
Simplicidade: Evite complexidade desnecessária. Mantenha o código o mais simples possível, sem comprometer a funcionalidade.
Consistência: Siga padrões de codificação consistentes em todo o código-base. Isso inclui convenções de nomenclatura, estilo de codificação e formatação.
Manutenibilidade: O código deve ser fácil de modificar e estender sem introduzir bugs ou efeitos colaterais indesejados.
Eficiência: Escreva código eficiente e otimizado, mas sem sacrificar a clareza e a legibilidade.
Testabilidade: Escreva código que seja fácil de testar, o que significa que as unidades individuais de código podem ser testadas de forma isolada.
Para aprofundamento, acesse: https://github.com/free-educa/books/blob/main/books/Codigo%20Limpo%20-%20Completo%20PT.pdf
