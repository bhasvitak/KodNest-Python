def check_sign(number):
    if number > 0:
        return "Positive"
    elif number == 0:
        return "Zero"
    else:
        return "Negative"
    pass

number = int(input())
result = check_sign(number)
print(result)