def convert_to_uppercase(names):
    # Write your list comprehension here
    return [i.upper() for i in names]


n = int(input())
names = input().split()

uppercase_names = convert_to_uppercase(names)
print(*uppercase_names)