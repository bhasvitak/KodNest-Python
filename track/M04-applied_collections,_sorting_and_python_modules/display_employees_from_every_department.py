n = int(input())
departments = {}

for _ in range(n):
    data = input().split()
    department = data[0]
    employees = data[1:]

    departments[department] = employees

# Write your code here
for i in departments.keys():
    for j in departments[i]:
        print(f"{i}: {j}")