balance = int(input())

try:
    if balance < 0:
        raise ValueError
    print("Valid balance")
except ValueError:
    print("Invalid balance")