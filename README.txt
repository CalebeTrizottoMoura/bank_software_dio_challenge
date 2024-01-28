# Controle Bancário

Um programa simples de controle bancário em Python.

## Tela inicial

================ MENU PRINCIPAL ================
1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair

Escolha uma opção: 

- Caso seja escolhido uma letra ou número não pertencente ao menu, uma mensagem de advertência e enviada. 

## Funcionalidades

### 1. Depositar
- Permite ao usuário realizar depósitos em sua conta bancária;
- Aceita depósitos de até 2 casas decimais, separadas por um ponto ".";
- Não permite a inserção de números negativos ou letras;
- Todos os depósitos estão armazenados em uma variável.

### 2. Sacar
- Permite ao usuário realizar saques da conta bancária;
- Não permite saques de números negativos ou letras;
- Limite máximo por saque: R$ 500,00;
- Limite máximo de saques diários: 3;
- Saldo insuficiente: a transação será recusada se o valor do saque exceder o saldo disponível na conta;
- Quantidade máxima de saques diários excedida: o usuário será notificado e orientado a tentar novamente no dia seguinte;
- Todos os saques estão armazenados em uma variável.

### 3. Extrato
- Exibe o extrato das transações, incluindo depósitos, saques e o saldo atual da conta, em ordem cronológica;
- Se o extrato estiver em branco, é exibido a seguinte mensagem: Não foram realizadas movimentações;
- Todos os valores exibidos estão no seguinte formato: R$ xxxx.xx 

## Requisitos
- Python 3