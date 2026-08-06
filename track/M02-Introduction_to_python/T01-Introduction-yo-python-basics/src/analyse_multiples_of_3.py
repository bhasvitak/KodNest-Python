limit = int(input())
target = int(input())

count = 0
total = 0
found = False

# Examine every number from 1 to the limit
for number in range(1, limit + 1):
    if number % 3 == 0:
        count += 1
        total += number
        if number == target:
            found = True

# Display the count, total and search result
print(f"Count: {count}")
print(f"Sum: {total}")

if found:
    print("Target Found: Yes")
else:
    print("Target Found: No")