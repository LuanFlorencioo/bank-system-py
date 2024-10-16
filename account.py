from utils.get_current_date import get_current_date

class Account:
    def __init__(self) -> None:
        self.balance = float(0)
        self.extracts = []
        self.withdrawal_count = 0
    
    def create_transaction(self, is_deposit = True, value = 0):
        transaction = {
            "type": "deposit" if is_deposit else "withdrawal",
            "value": value,
            "date": get_current_date()
        }

        if is_deposit:
            self.balance += value
            print(f"✔ DEPÓSITO REALIZADO - ({transaction['date']})")
            print(f"- Valor de R$ {value:.2f} foi depositado de sua conta\n")
        
        else:
            self.withdrawal_count += 1
            self.balance -= value
            print(f"✔ SAQUE REALIZADO - ({transaction['date']})")
            print(f"- Valor de R$ {value:.2f} foi sacado de sua conta\n")
        
        self.extracts.append(transaction)

    def get_extracts(self):
        is_extracts_empty = len(self.extracts) == 0
        if is_extracts_empty:
            print("Não foram realizadas movimentações")
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            for transaction in self.extracts:
                transaction_type = "🟢 DEPÓSITO" if transaction["type"] == "deposit" else "🔴 SAQUE"
                print(f"| {transaction["date"]} | {transaction_type} | R$ {transaction["value"]:.2f}")

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print(f"Seu saldo atual é de: R$ {self.balance:.2f}")
