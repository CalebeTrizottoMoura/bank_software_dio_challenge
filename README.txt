# Controle Bancário Simples

Um programa simples de controle bancário em Python.

## Funcionalidades

### 1. Depositar

Permite ao usuário realizar depósitos na conta bancária.

### 2. Sacar

Permite ao usuário realizar saques da conta bancária, com as seguintes restrições:
- Limite máximo por saque: R$ 500,00
- Limite máximo de saques diários: 3
- Saldo insuficiente: A transação será recusada se o valor do saque exceder o saldo disponível na conta.
- Quantidade máxima de saques diários excedida: O usuário será notificado e orientado a tentar novamente no dia seguinte.

### 3. Extrato

Exibe o extrato das transações, incluindo depósitos, saques e o saldo atual da conta, em ordem cronológica.

## Requisitos

- Python 3.x