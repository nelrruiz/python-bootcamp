class NegativeDepositError(ValueError):
    def __init__(self, *args):
        super().__init__("Deposit amount cannot be negative",*args)
    # raise ValueError("Deposit amount cannot be negative")

class OverwithdrawError(ValueError):
    def __init__(self, *args):
        super().__init__("amount is greater than balance",*args)

class NegativeBalanceError(ValueError):
    def __init__(self, *args):
        super().__init__("amount cannot be negative",*args)



class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount < 0:
            raise NegativeDepositError()
        self._balance += amount


    def withdraw(self, amount):
        if amount <= 0:
            raise NegativeBalanceError()
        if amount > self._balance:
            raise OverwithdrawError()
        
        self._balance -= amount

    def print_balance(self):
        print(self._balance)


bank_account = BankAccount(1000)
bank_account.deposit(1)
bank_account.print_balance()
bank_account.withdraw(2000)
bank_account.print_balance()

# print(bank_account)
