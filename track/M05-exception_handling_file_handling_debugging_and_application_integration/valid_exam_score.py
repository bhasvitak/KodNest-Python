score = int(input())

try:
    if score<0 or score>100:
        raise ValueError
    print("Valid score")
except ValueError:
    print("Invalid score")