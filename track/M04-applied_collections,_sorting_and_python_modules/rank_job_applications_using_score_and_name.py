n = int(input())
applications = []

for _ in range(n):
    name, score = input().split()
    applications.append((name, int(score)))

# Write your code here
sorted_applications = sorted(applications, key=lambda application: (-application[1], application[0]))
for i in sorted_applications:
    print(*i)