n = int(input())
employees = []

for _ in range(n):
    name, salary = input().split()
    employees.append((name, int(salary)))

# Write your code here
sorted_employees = sorted(employees,key=lambda employee:employee[1])
for i in sorted_employees:
    print(*i)