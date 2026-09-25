n = int(input())
departments = {}

for _ in range(n):
    data = input().split()
    department = data[0]
    salaries = list(map(int, data[1:]))

    departments[department] = salaries

for i in departments:
    print(f"{i}: {sum(departments[i])}")