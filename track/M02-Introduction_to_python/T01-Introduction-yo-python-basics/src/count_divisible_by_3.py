starting_number = int(input())
ending_number = int(input())

count = 0

for number in range(starting_number, ending_number + 1):
    if number % 3 == 0:
        count += 1

print(f"Divisible by 3: {count}")