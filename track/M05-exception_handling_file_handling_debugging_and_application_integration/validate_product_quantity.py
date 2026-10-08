q = int(input())

# Write your code here
try:
    if q <= 0:
        raise ValueError("Quantity must be at least 1")
    print("Valid quantity")
except ValueError as e:
    print(e)