value_count = int(input())
original_list = []

# Read and store all values using append()
for i in range(value_count):
    original_list.append(int(input()))

# Create an alias and a shallow copy
list2 = original_list
list3 = original_list.copy()

# Read position and value inputs
alias_position = int(input())
alias_value = int(input())
copy_position = int(input())
copy_value = int(input())

# Update values using 0-based indexing
list2[alias_position - 1] = alias_value
list3[copy_position - 1] = copy_value

# Count differing positions between original and copied list
different_positions = 0
for i in range(value_count):
    if original_list[i] != list3[i]:
        different_positions += 1

# Print outputs matching exact expected labels
print(f"Original List: {original_list}")
print(f"Alias List: {list2}")
print(f"Copied List: {list3}")

if original_list is list2:
    print("Alias Shares Original: Yes")
else:
    print("Alias Shares Original: No")

print(f"Different Positions: {different_positions}")