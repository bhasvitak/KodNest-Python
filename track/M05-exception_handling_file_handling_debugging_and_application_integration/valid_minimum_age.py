try:
    age = int(input())
    if age < 18:
        raise ValueError
    print("Eligible")
except ValueError:
    print("Invalid age")