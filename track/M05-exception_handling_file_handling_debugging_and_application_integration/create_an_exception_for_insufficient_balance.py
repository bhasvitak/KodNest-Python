class InsufficientBalanceError(Exception):
    pass

balance = int(input())
amount = int(input())

try:
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")
    print("Withdrawal allowed")
except InsufficientBalanceError as e:
    print(e)