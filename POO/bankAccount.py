class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}.El saldo actual es {self.balance}")
        else:
            print("No se puede depositar. Cuenta inactiva")

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}.El saldo actual es {self.balance}")
            else:
                print("Fondos insuficientes")
        else:
            print("No se puede retirar. Cuenta inactiva")

    def deactivate_account(self):
        self.active = False
        print("Cuenta desactivada.")

    def activate_account(self):
        self.active = True
        print("Cuenta activada")

account1 = BankAccount("Juan", 500)
account2 = BankAccount("Ana", 250)