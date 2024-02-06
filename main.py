from datetime import datetime
from typing import Any
import os
import time

def menu():
    menu = """================ MENU PRINCIPAL ================
1 - Depositar
2 - Sacar
3 - Extrato
4 - Criar Usuário (Gerência)
5 - Criar Conta (Gerência)
6 - Listar Usuários (Gerência)
7 - Listar Contas (Gerência)
8 - Sair

Escolha uma opção: """
    return menu

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_print_time(prompt):
    clear_terminal()
    print(prompt)
    time.sleep(3)

def get_space(prompt):
    while True:
        option = input(prompt)
        if option != " " and option != "," and option != ",," and option != "":
            return option
        clear_terminal()

def deposit_function(account_balance, deposits_history, deposits_history_date_time, /):
    while True:
        clear_terminal()
        print("================ DEPÓSITO ================")
        deposit_str = get_space("Quanto deseja depositar? ")
        if deposit_str.replace('.', '', 1).isdigit():
            deposit = float(deposit_str)
            if deposit > 0:
                clear_print_time("Depósito realizado com sucesso!")
                deposits_history.insert(len(deposits_history), deposit)
                deposits_history_date_time.insert(len(deposits_history), datetime.now().strftime("Data: %d/%m/%Y - Hora: %H:%M:%S"))
                account_balance += deposit
                return account_balance
            else:
                clear_print_time("Valor inválido. Por favor, digite novamente.")
        else:
            clear_print_time("Por favor, digite um valor válido.")

def withdraw_function(*, account_balance, daily_withdrawal, withdraw_history, withdraw_history_date_time):
    while True:
        clear_terminal()
        print("================ SAQUE ================")
        withdraw_str = get_space("Quanto deseja sacar? ")
        if withdraw_str.replace('.', '', 1).isdigit():
            withdraw = float(withdraw_str)
            if daily_withdrawal < DAILY_WITHDRAWAL_LIMIT and withdraw <= VALUE_WITHDRAW_LIMIT and withdraw <= account_balance:
                clear_print_time("Saque realizado com sucesso!")
                withdraw_history.insert(len(withdraw_history), withdraw)
                withdraw_history_date_time.insert(len(withdraw_history), datetime.now().strftime("Data: %d/%m/%Y - Hora: %H:%M:%S"))
                account_balance -= withdraw
                daily_withdrawal += 1
                return account_balance, daily_withdrawal
            elif withdraw > VALUE_WITHDRAW_LIMIT:
                clear_print_time("O valor excede o limite máximo por saque. Tente novamente!")
            elif withdraw > account_balance:
                clear_print_time("Saldo insuficiente. Verifique seu extrato!")
                return None
            else:
                clear_print_time("Quantidade máxima de saques diários excedida. Tente novamente amanhã!")
                return None
        else:
            clear_print_time("Por favor, digite um valor válido.")

def extract(deposits_history, withdraw_history, /, *, deposits_history_date_time, withdraw_history_date_time):
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

def confirmation_address(formatted_address):
    while True:
        clear_terminal()
        response = get_space(f"""Só para confirmar, este seria o endereço completo?

{formatted_address.upper()}

1 - SIM
2 - NÃO
                        
Digite aqui o número da sua resposta: """)
        if response == "1":
            exit = 1
            return exit
        elif response == "2":
            clear_print_time("Ok, digite novamente o seu endereço.")
            back = 2
            return back
        else:
            clear_print_time("Ops! Opção inválida.\n\nEscolha novamente uma opção.")

def cpf_function(user_list):
    while True:
        clear_terminal()
        cpf_first = get_space("Digite o CPF com 11 dígitos: ")
        cpf = cpf_first.replace(".", "").replace("-", "")
        cpf_control = 0
        for i in range(len(user_list)):
            if user_list[i]["CPF"] == cpf:
                cpf_control = 1
        if len(cpf) != 11 or not cpf.isdigit():
            clear_print_time("CPF inválido!")
        elif cpf_control > 0:
            clear_print_time("O CPF já está cadastrado no sistema.") 
            clear_terminal()
            print("Hum! E o que deseja fazer agora?\n") 
            print("1 - Digitar um novo CPF") 
            print("2 - Voltar ao menu principal") 
            new_option = int(get_space("\nDigite o número da sua opção: "))
            if new_option == 2:
                return None
        else:
            return cpf

def format_cpf(cpf):
    return "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])

def address_function():
    while True:
        clear_terminal()
        road = get_space("Agora, digite o endereço!\n\nQual o nome da rua? ")
        clear_terminal()
        address_number = get_space("Número da residência? ")
        clear_terminal()
        neighborhood = get_space("Em qual bairro? ")
        clear_terminal()
        city = get_space("Qual cidade? ")
        clear_terminal()
        estate = get_space("Para concluir, é só digitar a sigla do estado: ")
        clear_terminal()
        formatted_address = f"{road.title()}, {address_number} - {neighborhood.title()} - {city.title()}/{estate.upper()}"
        control = confirmation_address(formatted_address)
        if control == 1:
            return formatted_address

def date_birth_function():
    while True:
        clear_terminal()
        date_birth_first = get_space("Digite a data de nascimento (DD/MM/AAAA ou DDMMAAAA): ")
        date_birth_second = date_birth_first.replace("/", "", 2)
        if not date_birth_second.isdigit() or len(date_birth_second) != 8:
            clear_terminal()
            print("Por favor, digite uma data válida neste formato: DD/MM/AAAA ou DDMMAAAA")
            input("\nAperte ENTER para digitar novamente a sua data de nascimento.")
        else:
            date_birth = datetime.strptime(date_birth_second, "%d%m%Y")
            return date_birth.strftime("%d/%m/%Y")

def create_user(user_list, user_number: int) -> int:
    clear_terminal()
    name = get_space("Digite o nome completo do(a) solicitante: ")
    date_birth = date_birth_function()
    if (cpf := cpf_function(user_list)) is None: 
        return None
    address = address_function()
    new_user = {"name": name, "data de nascimento": date_birth, "CPF": cpf, "endereço": address}
    user_list.insert(user_number, new_user)
    user_number += 1
    clear_terminal()
    return user_number

def user_list_function(user_list):
    clear_terminal()
    print("================ LISTAR USUÁRIOS ================")
    if user_list:
        for i in range(len(user_list)):
            print(f"Nome: {user_list[i]['name'].title()}")
            print(f"Data de nascimento: {user_list[i]['data de nascimento']}")
            print(f"CPF: {format_cpf(user_list[i]['CPF'])}")
            print(f"Endereço: {user_list[i]['endereço']}")
            if i + 1 != len(user_list):
                print("=================================================")
        input("\nAperte ENTER para voltar ao menu principal.")
    else:
        print("Não há dados para mostrar.")
        time.sleep(3)

def create_current_account(user_list, current_account_number: int) -> int:
    clear_terminal()
    print("================ CRIAR CONTA CORRENTE ================")
    while True: 
        new_cpf = input("Para continuarmos, preciso que digite o CPF com 11 dígitos: ")
        cpf = new_cpf.replace(".", "").replace("-", "")
        cpf_control = 0
        for i in range(len(user_list)):
            if user_list[i]["CPF"] == cpf:
                cpf_control = 1
                index = i
                clear_print_time("CPF encontrado!")
        if len(cpf) != 11 or not cpf.isdigit():
            clear_print_time("CPF inválido!")
        elif cpf_control > 0:
            if len(user_list[index]) > 4:
                user_list[index]["conta corrente"].append(current_account_number)
                current_account_number += 1
                clear_print_time("Conta cadastrada com sucesso!")
                return current_account_number
            else:
                new_account = {"agência": "0001", "conta corrente": [current_account_number]}
                user_list[index].update(new_account)
                current_account_number += 1
                clear_print_time("Conta cadastrada com sucesso!")
                return current_account_number
        else:
            clear_print_time("Puxa! Parece que o CPF não está cadastrado.")
            print("\nVoltando ao menu principal.")
            time.sleep(3)
            break

def list_current_account(user_list):
    clear_terminal()
    print("================ LISTAGEM DE CONTAS ================")
    control_first = 0
    control_second = False
    for i in range(len(user_list)):
        if len(user_list[i]) > 4:
            control_first += 1
    for i in range(len(user_list)):
        if len(user_list[i]) > 4:
            print(f"Titular: {user_list[i]['name'].title()}")
            print(f"Agência: {user_list[i]['agência']}")
            current_account = " / ".join(map(str, user_list[i]['conta corrente']))
            print(f"Conta Corrente: {current_account}")
            control_second = True
            if i + 1 != control_first:
                print("====================================================")
    if control_second != True:
        print("Não há dados para mostrar.")
        time.sleep(3)
    else:
        input("\nAperte ENTER para voltar ao menu principal.")

VALUE_WITHDRAW_LIMIT = 500
DAILY_WITHDRAWAL_LIMIT = 3

account_balance = 0
user_list = []
deposits_history_date_time = []
withdraw_history_date_time = []
withdraw_history = []
deposits_history = []
daily_withdrawal = 0
user_number = 0
current_account_number = 1

while True:
    clear_terminal()
    option = float(get_space(menu()))
    if option == 1:
        account_balance = deposit_function(account_balance, deposits_history, deposits_history_date_time)
    elif option == 2:
        result = withdraw_function(
            account_balance=account_balance, 
            daily_withdrawal=daily_withdrawal, 
            withdraw_history=withdraw_history, 
            withdraw_history_date_time=withdraw_history_date_time,
            )
        if result is not None:
            account_balance, daily_withdrawal = result
        else:
            clear_print_time("Operação de saque cancelada.")
            
    elif option == 3:
        extract(
            deposits_history, 
            withdraw_history, 
            deposits_history_date_time=deposits_history_date_time, 
            withdraw_history_date_time=withdraw_history_date_time,
            )
    elif option == 4:
        user_number = create_user(user_list, user_number)
        if user_number is not None: 
            print("Usuário(a) cadastrado(a) com sucesso!")
            time.sleep(3)
    elif option == 5:
        current_account_number = create_current_account(user_list, current_account_number)
    elif option == 6:
        user_list_function(user_list)
    elif option == 7:
        list_current_account(user_list)
    elif option == 8:
        clear_print_time("Volte sempre!")
        break
    else:
        clear_print_time("Por favor, digite uma opção válida.")