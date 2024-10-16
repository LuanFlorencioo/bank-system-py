from services.account import Account
from utils.press_enter_message import press_enter_message

main_menu = """
Escolha um das seguintes operações abaixo:
◤------------------------------------◥

[1] → 💰 depositar um valor;
[2] → 🏧 sacar um valor;
[3] → 🧾 conferir extrato bancário;
[4] → 👀 ver saldo bancário;
[0] → sair do sistema bancário;

◣------------------------------------◢
Insira o dígito referente a operação: """

current_user = Account()

print("\n_____ Seja-vindo(a) ao Sistema Bancário _____\n")

while True:
    option = input(main_menu)
    is_option_exit = option == "0"
    is_option_deposit = option == "1"
    is_option_withdrawal = option == "2"
    is_option_extract = option == "3"
    is_option_balance = option == "4"

    if is_option_exit:
        close_confirmation = input("Tem certeza que deseja encerrar sua sessão?\n[1] - Sim\n[2] - Não\n")
        
        if close_confirmation == "1":
            print("Encerrando sua sessão...")
            print("Agradecemos sua presença. Até logo! 👋")
            break

    elif is_option_deposit:
        print("Você escolheu a operação de depósito 💰")
        deposit_value = float(input("Insira o valor a ser depositado:\n↳ R$ "))

        if deposit_value > 0:
            current_user.create_transaction(is_deposit=True, value=deposit_value)
        else:
            print("❌ Valor inválido! O valor não pode ser zero\n")
        
        press_enter_message()

    elif is_option_withdrawal:
        if current_user.balance == 0:
            print("Não há saldo em sua conta! É preciso haver saldo positivo em sua conta\n")
        elif current_user.withdrawal_count == 3:
            print("❌ Você atingiu seu limite de saque diário (3 saques diários)!")
        else:
            print("Você escolheu a operação de saque 🏧")
            withdrawal_value = float(input("Insira o valor a ser sacado:\n↳ R$ "))

            if withdrawal_value > current_user.balance:
                print("❌ Saldo insuficiente para realizar este saque\n")
            elif withdrawal_value > 500:
                print("❌ Valor muito alto! Não é possível realizar um saque acima de R$ 500,00\n")
            elif withdrawal_value == 0:
                print("❌ Valor inválido! O valor não pode ser zero\n")
            else:
                current_user.create_transaction(is_deposit=False, value=withdrawal_value)

        press_enter_message()

    elif is_option_extract:
        print("Você escolheu a operação de conferir extrato bancário 🧾")
        current_user.get_extracts()
        press_enter_message()

    elif is_option_balance:
        print("Você escolheu a operação de visualização de saldo 👀")
        print(f"Saldo: R$ {current_user.balance:.2f} -----\n")
        press_enter_message()