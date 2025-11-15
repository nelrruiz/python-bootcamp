class CashPayment:
    def __init__(self, amount):
        self.amount = amount

    def total(self):
        return self.amount


class CreditPayment:
    def __init__(self, amount, limit):
        self.amount = amount
        self.limit = limit

    def total(self):
        """Raise error if amount is beyond limit"""
        if self.amount > self.limit:
            print(f"Amount is beyond limit.") #nels code
            return 0 #nels code
            raise ValueError("Amount must be greater than or equal to limit.") #stephen's

class OnlinePayment:
    def __init__(self, amount, fee):
        """Set attributes here"""
        self.amount = amount
        self.fee = fee

    def total(self):
        """Return amount + fee"""
        return self.amount + self.fee
    
    def __repr__(self):
        return f"OnlinePayment(amount={self.amount}, fee={self.fee}, total = self.total())"

class DiscountedPayment:
    def __init__(self, amount, discount):
        """Set attributes here"""
        self.amount = amount
        self.discount = discount

    def total(self):
        """Return amount - discount"""
        return self.amount - self.discount

payments = [
    CashPayment(1_000),
    CashPayment(10_000),
    OnlinePayment(1_000, 100),
    CreditPayment(1_000,500),
    DiscountedPayment(1_000, 10)
]

for payment in payments:
    print(payment.total())
