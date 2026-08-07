word = input()

first = int(input())
second = int(input())
third = int(input())

numbers = [first, second, third]
record = (first, second, third)

# Slice the string, list and tuple
print(f"Middle: {word[1:-1]}")
print(f"First Two: {numbers[0:2]}")
print(f"Reversed Tuple: {record[::-1]}")