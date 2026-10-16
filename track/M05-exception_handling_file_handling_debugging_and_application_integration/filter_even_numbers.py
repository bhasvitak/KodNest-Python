def is_even(number):
    # TODO: Implement logic to check if the number is even
    return number % 2 == 0

# TODO: Use filter() to extract even numbers from user_numbers
user_numbers = list(map(int, input().split()))
result = list(filter(is_even, user_numbers))
print(result)