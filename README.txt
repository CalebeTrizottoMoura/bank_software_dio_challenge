CONTROLE BANCÁRIO:
Um programa simples de controle bancário em Python.


TELA INICIAL:
"""================ MENU PRINCIPAL ================
1 - Depositar
2 - Sacar
3 - Extrato
4 - Criar Usuário (Gerência)
5 - Criar Conta (Gerência)
6 - Listar Usuários (Gerência)
7 - Listar Contas (Gerência)
8 - Sair

Escolha uma opção: """

Caso seja escolhido uma letra ou número não pertencente ao menu, uma mensagem de advertência e enviada.


FUNCIONALIDADES:
1. Depositar:
Permite ao usuário realizar depósitos em sua conta bancária;
Aceita depósitos de até 2 casas decimais, separadas por um ponto ".";
Não permite a inserção de números negativos ou letras;
Todos os depósitos estão armazenados em uma variável.

2. Sacar:
Permite ao usuário realizar saques da conta bancária;
Não permite saques de números negativos ou letras;
Limite máximo por saque: R$ 500,00;
Limite máximo de saques diários: 3;
Saldo insuficiente: a transação será recusada se o valor do saque exceder o saldo disponível na conta;
Quantidade máxima de saques diários excedida: o usuário será notificado e orientado a tentar novamente no dia seguinte;
Todos os saques estão armazenados em uma variável.

3. Extrato:
Exibe o extrato das transações, incluindo depósitos, saques e o saldo atual da conta, em ordem cronológica;
Se o extrato estiver em branco, é exibida a seguinte mensagem: Não foram realizadas movimentações;
Todos os valores exibidos estão no seguinte formato: R$ xxxx.xx

4. Criar Usuário (Gerência):
Permite a criação de um novo usuário no sistema;
Solicita informações como nome, data de nascimento, CPF e endereço;
Garante a unicidade do CPF, alertando se o CPF já estiver cadastrado no sistema;
Exibe uma confirmação do endereço fornecido antes de finalizar o cadastro.

5. Criar Conta (Gerência):
Permite a criação de uma nova conta corrente associada a um usuário existente;
Solicita o CPF do titular para localizar o usuário no sistema;
Associa a nova conta ao usuário encontrado ou cria um novo usuário se o CPF não estiver cadastrado;
Exibe informações sobre a conta criada, incluindo agência e número da conta.

6. Listar Usuários (Gerência):
Apresenta uma lista de todos os usuários cadastrados no sistema;
Mostra detalhes como nome, data de nascimento, CPF e endereço;
Permite uma visão abrangente dos usuários cadastrados no sistema.

7. Listar Contas (Gerência):
Apresenta uma lista de todas as contas correntes associadas aos usuários cadastrados;
Mostra detalhes como titular, agência e número da conta;
Facilita a visualização e gestão das contas correntes no sistema.


REQUISITOS:
Python 3