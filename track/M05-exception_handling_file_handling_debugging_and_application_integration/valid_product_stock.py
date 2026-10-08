stock = int(input())

try:
    if stock < 0:
        raise ValueError
    print("Valid stock")
except ValueError:
    print("Invalid stock")