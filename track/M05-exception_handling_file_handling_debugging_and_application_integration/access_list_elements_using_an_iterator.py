n = int(input())
students = [input() for _ in range(n)]

# Write your code here
stu_it = iter(students)
for i in range(n):
    print(next(stu_it))