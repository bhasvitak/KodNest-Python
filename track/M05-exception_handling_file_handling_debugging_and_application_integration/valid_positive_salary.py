salary = int(input())

try:
    if salary <= 0:
        raise ValueError
    print("Valid salary")
except ValueError:
    print("Invalid salary")