# Controle Bancário

Um programa simples de controle bancário em Python.

## Funcionalidades

### 1. Depositar
- Permite ao usuário realizar depósitos em sua conta bancária;
- Aceita depósitos de até 2 casas decimais, separadas por um ponto ".";
- Não permite a inserção de números negativos ou letras.

### 2. Sacar
- Permite ao usuário realizar saques da conta bancária;
- Não permite saques de números negativos ou letras;
- Limite máximo por saque: R$ 500,00;
- Limite máximo de saques diários: 3;
- Saldo insuficiente: a transação será recusada se o valor do saque exceder o saldo disponível na conta;
- Quantidade máxima de saques diários excedida: o usuário será notificado e orientado a tentar novamente no dia seguinte.

### 3. Extrato
- Exibe o extrato das transações, incluindo depósitos, saques e o saldo atual da conta, em ordem cronológica.

## Requisitos
- Python 3.x