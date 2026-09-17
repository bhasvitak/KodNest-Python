n = int(input())
temperatures = list(map(int, input().split()))

# Write your code here
print(*sorted(temperatures,reverse = True))