from datetime import datetime
import os
import time

VALUE_WITHDRAW_LIMIT = 500
DAILY_WITHDRAWAL_LIMIT = 3

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

account_balance = 0
deposits_history = []
deposits_history_date_time = []
withdraw_history = []
withdraw_history_date_time = []
daily_withdrawal = 0

menu = """================ MENU PRINCIPAL ================
1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair

Escolha uma opção: """

while True:
    clear_terminal()
    option = float(input(menu))
    if option == 1:
        while True:
            clear_terminal()
            print("================ DEPÓSITO ================")
            deposit_str = input("Quanto deseja depositar? ")
            if deposit_str.replace('.', '', 1).isdigit():
                deposit = float(deposit_str)
                if deposit > 0:
                    clear_terminal()
                    print("Depósito realizado com sucesso!")
                    time.sleep(2)
                    deposits_history.insert(len(deposits_history), deposit)
                    deposits_history_date_time.insert(len(deposits_history), datetime.now().strftime("Data: %d/%m/%Y - Hora: %H:%M:%S"))
                    account_balance += deposit
                    break
                else:
                    clear_terminal()
                    print("Valor inválido. Por favor, digite novamente.")
                    time.sleep(3)
            else:
                clear_terminal()
                print("Por favor, digite um valor válido.")
                time.sleep(3)
    elif option == 2:
        while True:
            clear_terminal()
            print("================ SAQUE ================")
            withdraw_str = input("Quanto deseja sacar? ")
            if withdraw_str.replace('.', '', 1).isdigit():
                withdraw = float(withdraw_str)
                if daily_withdrawal < DAILY_WITHDRAWAL_LIMIT and withdraw <= VALUE_WITHDRAW_LIMIT and withdraw <= account_balance:
                    clear_terminal()
                    print("Saque realizado com sucesso!")
                    time.sleep(2)
                    withdraw_history.insert(len(withdraw_history), withdraw)
                    withdraw_history_date_time.insert(len(withdraw_history), datetime.now().strftime("Data: %d/%m/%Y - Hora: %H:%M:%S"))
                    account_balance -= withdraw
                    daily_withdrawal += 1
                    break
                elif withdraw > VALUE_WITHDRAW_LIMIT:
                    clear_terminal()
                    print("O valor excede o limite máximo por saque. Tente novamente!")
                    time.sleep(3)
                elif withdraw > account_balance:
                    clear_terminal()
                    print("Saldo insuficiente. Verifique seu extrato!")
                    time.sleep(3)
                    break
                else:
                    clear_terminal()
                    print("Quantidade máxima de saques diários excedida. Tente novamente amanhã!")
                    time.sleep(3)
                    break
            else:
                clear_terminal()
                print("Por favor, digite um valor válido.")
                time.sleep(3)
    elif option == 3:
        clear_terminal()
        print("================ EXTRATO ================")
        if len(deposits_history) != 0 or len(withdraw_history) != 0:
            combined_history = list(zip(deposits_history_date_time, deposits_history, ['deposit'] * len(deposits_history))) + \
                               list(zip(withdraw_history_date_time, withdraw_history, ['withdraw'] * len(withdraw_history))) 
            combined_history_sorted = sorted(combined_history, key=lambda x: x[0])   
            for date_time, amount, transaction_type in combined_history_sorted:
                if transaction_type == 'deposit':
                    print(f"{date_time} - Valor de entrada: R$ {amount:.2f}")
                elif transaction_type == 'withdraw':
                    print(f"{date_time} - Valor de saída: R$ {amount:.2f}")
            print(f"\nSaldo atual: R$ {account_balance:.2f}\n")
            input("Aperte ENTER para voltar ao menu principal.")
        else:
            print("Não foram realizadas movimentações.")
            time.sleep(3)
    elif option == 4:
        clear_terminal()
        print("SAINDO...")
        time.sleep(2)
        break
    else:
        clear_terminal()
        print("Por favor, digite uma opção válida.")
        time.sleep(3)