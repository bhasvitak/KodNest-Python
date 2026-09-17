n = int(input())
marks = list(map(int, input().split()))

# Write your code here
print(*sorted(marks))
print(*sorted(marks, reverse=True))