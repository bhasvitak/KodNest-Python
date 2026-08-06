# Read how many numbers will be entered
number_count = int(input())

# Initialize counters and total
positive_count = 0
negative_count = 0
zero_count = 0
total = 0

# Process each number
for number in range(number_count):
    number = int(input())
    total += number

    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

# Display results
print(f"Positive Count: {positive_count}")
print(f"Negative Count: {negative_count}")
print(f"Zero Count: {zero_count}")
print(f"Total: {total}")