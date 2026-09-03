from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    # Add abstract process_payment()
    @abstractmethod
    def process_payment(self):
        pass


class UPIPayment(PaymentProcessor):
    def __init__(self, amount):
        self.amount = amount

    # Implement process_payment()
    def process_payment(self):
        return f"UPI Payment: {self.amount}"


class CardPayment(PaymentProcessor):
    def __init__(self, amount):
        self.amount = amount

    # Implement process_payment()
    def process_payment(self):
        return f"Card Payment: {self.amount}"


class NetBankingPayment(PaymentProcessor):
    def __init__(self, amount):
        self.amount = amount

    # Implement process_payment()
    def process_payment(self):
        return f"Net Banking Payment: {self.amount}"


upi_amount = int(input())
card_amount = int(input())
net_banking_amount = int(input())

# Create the three objects
u = UPIPayment(upi_amount)
c = CardPayment(card_amount)
n = NetBankingPayment(net_banking_amount)

# Store them in one list
lst = [u, c, n]

# Process them using one loop
for i in lst:
    print(i.process_payment())