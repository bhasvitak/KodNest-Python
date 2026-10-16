def to_uppercase(string):
    # TODO: Implement logic to convert string to uppercase
    return string.upper()

# TODO: Use map() to convert user_strings to uppercase
user_strings = list(map(str, input().split()))  # List of strings for conversion
result = list(map(to_uppercase, user_strings))
print(result)