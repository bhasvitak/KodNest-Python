n = int(input())
students = [input() for _ in range(n)]
k = int(input())
# Write your code here
s_it = iter(students)
if k == 0:
    print("No students called")
elif k > n:
    for i in range(n):
        print(next(s_it))
else:
    for i in range(k):
        print(next(s_it))