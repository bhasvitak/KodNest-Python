number = int(input())
sum_of_digits = 0

while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10

print(f"Sum of Digits: {sum_of_digits}")