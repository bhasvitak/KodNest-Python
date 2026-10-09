class InvalidOrderQuantityError(Exception):
    pass

quantity = int(input())

# Write your code here
try:
    if quantity < 1 or quantity > 20:
        raise InvalidOrderQuantityError("Order quantity must be between 1 and 20")
    print("Valid order quantity")
except InvalidOrderQuantityError as e:
    print(e)