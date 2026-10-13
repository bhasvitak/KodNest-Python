class InvalidAmountError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

balance = int(input())
amount = int(input())

# Write your code here
try:
    if amount <= 0:
        raise InvalidAmountError("Withdrawal amount must be greater than 0")
    elif amount > balance:
        raise InsufficientBalanceError("Insufficient balance")
    print("Withdrawal successful")
except Exception as e:
    print(e)